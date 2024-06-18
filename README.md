# LangGraph_Multithread_RAG_Tools

### Sample Outputs:
Thread ID: 2
User: Hi. I am Aditya.
================================ Human Message =================================

Hi. I am Aditya.
================================== Ai Message ==================================

Hello, Aditya! How can I assist you today?
Thread ID: 4
User: Hi. I am Yash.
================================ Human Message =================================

Hi. I am Yash.
================================== Ai Message ==================================

Hello, Yash! How can I assist you today?
Thread ID: 2
User: What's my name?
================================ Human Message =================================

What's my name?
================================== Ai Message ==================================

You mentioned that your name is Aditya. How can I help you today, Aditya?
Thread ID: 4

User: What's my name?
================================ Human Message =================================

What's my name?
================================== Ai Message ==================================

Your name is Yash. How can I help you today, Yash?
Thread ID: 4
User: Tell me the weather forecast for HSR Bengaluru today.
================================ Human Message =================================

Tell me the weather forecast for HSR Bengaluru today.
================================== Ai Message ==================================
Tool Calls:
  tavily_search_results_json (call_F1JlTjv2cSA4lSdDP5MaUpIR)
 Call ID: call_F1JlTjv2cSA4lSdDP5MaUpIR
  Args:
    query: weather forecast HSR Bengaluru today
================================= Tool Message =================================
Name: tavily_search_results_json

[{"url": "https://www.weatherapi.com/", "content": "{'location': {'name': 'Bengaluru', 'region': 'Karnataka', 'country': 'India', 'lat': 12.98, 'lon': 77.58, 'tz_id': 'Asia/Kolkata', 'localtime_epoch': 1718711847, 'localtime': '2024-06-18 17:27'}, 'current': {'last_updated_epoch': 1718711100, 'last_updated': '2024-06-18 17:15', 'temp_c': 30.3, 'temp_f': 86.5, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 13.6, 'wind_kph': 22.0, 'wind_degree': 250, 'wind_dir': 'WSW', 'pressure_mb': 1010.0, 'pressure_in': 29.83, 'precip_mm': 0.01, 'precip_in': 0.0, 'humidity': 62, 'cloud': 50, 'feelslike_c': 32.8, 'feelslike_f': 91.0, 'windchill_c': 28.1, 'windchill_f': 82.6, 'heatindex_c': 29.4, 'heatindex_f': 84.8, 'dewpoint_c': 18.3, 'dewpoint_f': 64.9, 'vis_km': 8.0, 'vis_miles': 4.0, 'uv': 6.0, 'gust_mph': 18.1, 'gust_kph': 29.2}}"}, {"url": "https://www.accuweather.com/en/in/hosur-sarjapur-road-layout/3352280/weather-forecast/3352280", "content": "Hosur Sarjapur Road Layout, Karnataka, India Weather Forecast, with current conditions, wind, air quality, and what to expect for the next 3 days."}]
================================== Ai Message ==================================

The weather forecast for HSR Layout, Bengaluru today is as follows:

- **Condition:** Partly cloudy
- **Temperature:** 30.3°C (86.5°F)
- **Feels Like:** 32.8°C (91.0°F)
- **Wind:** 22.0 kph (13.6 mph) from the WSW
- **Humidity:** 62%
- **Precipitation:** 0.01 mm
- **Visibility:** 8.0 km
- **UV Index:** 6 (Moderate)

Would you like to know anything else?
