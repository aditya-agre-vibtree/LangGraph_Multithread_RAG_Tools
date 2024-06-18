from typing import Annotated

from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import ToolNode, tools_condition




from dotenv import load_dotenv
load_dotenv()

tool = TavilySearchResults(max_results=2)
tools = [tool]

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # openai_api_key=openai.api_key,  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
)
# Modification: tell the LLM which tools it can call
llm_with_tools = llm.bind_tools(tools)




class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)


from langgraph.checkpoint.sqlite import SqliteSaver

memory = SqliteSaver.from_conn_string(":memory:")


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=[tool])
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")
graph = graph_builder.compile(checkpointer=memory)


def create_config(thread_id):
    config = {"configurable": {"thread_id": thread_id}}
    return config
# user_input = "Hi there! My name is Will."
#
# for event in events:
#     event["messages"][-1].pretty_print()


from langchain_core.messages import BaseMessage
while True:
    thread_id = input("Thread ID: ")
    user_input_message  = input("User: ")

    config = create_config(thread_id)

    if user_input_message.lower() in ["quit", "exit", "q"]:
        print("Assistant: Goodbye!")
        break
    # The config is the **second positional argument** to stream() or invoke()!
    events = graph.stream(
        {"messages": [("user", user_input_message)]}, config, stream_mode="values"
    )

    for event in events:
        event["messages"][-1].pretty_print()
        # print(event["messages"][-1])

    # snapshot = graph.get_state(config)
    # print(snapshot)

