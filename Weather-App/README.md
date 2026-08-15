
Weather App

This is a command-line weather app that grabs live data from OpenWeatherMap. You can check the current temperature, humidity, pressure, wind speed, and get a quick weather description for pretty much any city on the planet.

What It Does

- You type in a city name.
- It pulls actual weather data from OpenWeatherMap.
- Shows you temperature, humidity, pressure, wind speed—basically all the main stuff.
- Output looks organized and easy to read.
- If something goes wrong (wrong city, API issues), it lets you know and won’t crash.
- You can search for as many cities as you want without restarting (thanks to recursion).
- Handles keyboard interrupts like Ctrl+C without freaking out.

Features

- Full weather report: temp, humidity, pressure, wind speed, description.
- Real-time: uses the requests library to fetch live data.
- Solid error messages: lets you know if the city isn’t found or if the API fails.
- Clean output: info lines up in a neat table—not messy.
- Search as many cities as you want without restarting.
- Catches KeyboardInterrupt, so you can shut it down without ugly errors.
- Parses JSON to pull data out of nested responses.
- Recursion lets you keep searching cities without loops.

How to Run

Step 1: Install the requests library
pip install requests

Step 2: Get API Key
- There’s an API key in the code already.
- Want your own? Sign up at https://openweathermap.org/api, grab your key.

Step 3: Run It
python weather_app.py

Example Output

Enter city name: London
========================================
Weather Information
========================================
City           : London
Country        : GB
Temperature    : 27.31°C
Description    : Overcast clouds
Humidity       : 52%
Pressure       : 1016 hPa
Wind Speed     : 4.12 m/s
Search for another city? (y/n): y

Enter city name: Tokyo
========================================
Weather Information
========================================
City           : Tokyo
Country        : JP
Temperature    : 24.44°C
Description    : Overcast clouds
Humidity       : 84%
Pressure       : 1013 hPa
Wind Speed     : 4.12 m/s
Search for another city? (y/n): n

Thank you for using the Weather App!

What I Learned

- Sending HTTP requests with Python requests.
- Figuring out how API endpoints, base URLs, and parameters work.
- Parsing JSON to dig out what I actually want.
- Checking response codes to catch errors.
- Lining up text output with f-strings and nice formatting.
- Graceful shutdown for user input—no ugly KeyboardInterrupt.
- Recursion to keep searching without loops.
- Passing parameters like city name, API key, units through the API.
- Digging into deep-nested dictionaries for real-world data.
- Connecting a Python app to live internet data—feels pretty satisfying.

Code Structure

def get_weather_data(city):
    # Builds the API request, sends it, returns JSON data.

def display_weather_info(weather_data):
    # Checks if API call worked, pulls out weather info, and prints it nicely.

def main():
    # Takes city input, fetches weather, shows output.
    # Keeps asking if you want to search again, uses recursion.
    # Handles KeyboardInterrupt for a clean exit.

API Response Structure

city name → weather_data["name"]
country → weather_data["sys"]["country"]
temperature → weather_data["main"]["temp"]
description → weather_data["weather"][0]["description"]
humidity → weather_data["main"]["humidity"]
pressure → weather_data["main"]["pressure"]
wind_speed → weather_data["wind"]["speed"]

Challenges

- Nested dictionaries: digging out weather[0]["description"] is actually awkward.
- Getting f-string formatting just right so columns line up.
- Handling API errors: catching when cod != 200 and showing a nice message.
- KeyboardInterrupt: letting users quit without staring at a traceback.
- Using recursion instead of a loop to repeat searches.
- Case sensitivity: turns out “Tokyo”, “tyoko”, or “TOKYO” all work fine.
- API key security: I realized hardcoding a key is risky if you share code publicly.

What Works

✓ Handles typos—if you type “Tyoko”, it tells you “city not found” and lets you try again.
✓ Lets you search a bunch of cities back-to-back, no restarts.
✓ Output is clean and easy to read.
✓ Error messages are clear—no confusion when something goes wrong.
✓ Friendly—thanks messages and gentle exits.

Things I Could Add

- Save favorite cities in a file.
- Display weather forecast (next five days).
- Show sunrise and sunset times.
- Let you pick units: Celsius, Fahrenheit, Kelvin.
- Store API key in environment variables—much safer.
- Search by coordinates.
- Show weather icons.
- Compare weather across cities.
- Add weather alerts.
- Local cache for cities (don't hammer API needlessly).

Why This Matters

This project proves I can:
- Use real APIs and work with live internet data.
- Handle errors and actually tell the user what happened.
- Write code that's organized—one function, one job.
- Make output look professional, not messy.
- Keep the app running smoothly with recursion.
- Handle user input calmly (no crashing).

Some key takeaways:
- Real apps rely on APIs.
- APIs send you JSON, which is just Python dictionaries most of the time.
- Error handling isn’t optional—things fail.
- User experience counts: formatting, messages, exits.
- Apps shouldn’t live in their own bubble—they connect to the real world.

This isn’t “just practicing.” It’s building something useful that talks to real servers.

---

Important Notes

Security Notice:
- The API key is hardcoded right now (not ideal for public repos).
- You should use environment variables in real projects:

import os
api_key = os.getenv("OPENWEATHER_API_KEY")

Set it up like this:
export OPENWEATHER_API_KEY="your_api_key_here"

That’s safer in the long run, but the current version works for learning.

Requirements:
- Python 3.6+
- requests library (pip install requests)
- Internet connection
- API key (already in code)

---

Real Output vs Expected

Test Case 1: Valid city (London)
✓ Shows weather correctly, asks if you want to search again, handles “y”

Test Case 2: Typo (Tyoko)
✓ Tells you “city not found,” lets you retry, gets weather for “Tokyo” after correction

Test Case 3: Exit
✓ Handles “n” gracefully, thanks the user, exits cleanly

All handled perfectly.

---

Next Steps

For next time:
- Move API key to environment variables.
- Add caching so it doesn’t keep calling API for the same city.
- Add a forecast.
- Maybe turn it into a web app using Flask.
- Deploy it somewhere so anyone can use it.

As it stands, this app is pretty robust for a learning project. Real apps are actually built this way!

Next up: more features and improvements 🌍


Before:

# Weather App

A fully-featured command-line weather application that fetches real weather data from OpenWeatherMap API. Get current temperature, humidity, pressure, wind speed, and weather description for any city in the world.

## What It Does

- Takes a city name as input
- Fetches live weather data from OpenWeatherMap API
- Displays detailed weather information (temperature, humidity, pressure, wind speed)
- Shows nicely formatted output
- Handles errors gracefully (city not found, API errors)
- Allows searching multiple cities in one session (recursion)
- Catches keyboard interrupts (Ctrl+C) gracefully

## Features

- **Complete weather data** - Temperature, humidity, pressure, wind speed, description
- **Real-time API integration** - Uses requests library to fetch live data
- **Error handling** - Handles invalid cities and API errors
- **Formatted output** - Professional-looking table with proper alignment
- **Multiple searches** - Search for multiple cities without restarting
- **Input validation** - Handles KeyboardInterrupt for user-friendly experience
- **JSON parsing** - Extracts nested data from API response
- **Recursion** - Uses recursion for repeat searches

## How to Run

**Step 1: Install Required Library**
```bash
pip install requests
```

**Step 2: Get API Key** (Optional - code already has one)
- Code has a working API key included
- To use your own: Go to https://openweathermap.org/api, sign up, get your API key

**Step 3: Run the App**
```bash
python weather_app.py
```

## Example Output

```
Enter city name: London
========================================
Weather Information
========================================
City           : London
Country        : GB
Temperature    : 27.31°C
Description    : Overcast clouds
Humidity       : 52%
Pressure       : 1016 hPa
Wind Speed     : 4.12 m/s
Search for another city? (y/n): y

Enter city name: Tokyo
========================================
Weather Information
========================================
City           : Tokyo
Country        : JP
Temperature    : 24.44°C
Description    : Overcast clouds
Humidity       : 84%
Pressure       : 1013 hPa
Wind Speed     : 4.12 m/s
Search for another city? (y/n): n

Thank you for using the Weather App!
```

## What I Learned

- **HTTP requests** - Using requests library to fetch data from real APIs
- **API endpoints** - Understanding base URLs, parameters, and how APIs work
- **JSON parsing** - Accessing nested dictionaries from API responses
- **Error handling** - Checking response codes and handling failures
- **String formatting** - Using f-strings with padding for aligned output
- **User input handling** - Catching KeyboardInterrupt for graceful shutdown
- **Recursion** - Using function to call itself for repeated searches
- **API parameters** - Passing city, API key, units, and additional data requests
- **Nested data access** - Accessing deeply nested dictionary values
- **Real-world integration** - Getting actual live data from internet

## Code Structure

```python
def get_weather_data(city):
    # Build API request with parameters
    # Send HTTP GET request to OpenWeatherMap
    # Return JSON response with weather data

def display_weather_info(weather_data):
    # Check if API response was successful (cod == 200)
    # Extract city, country, temperature, humidity, pressure, wind
    # Display formatted weather information

def main():
    # Get city name from user (with KeyboardInterrupt handling)
    # Call get_weather_data to fetch data
    # Call display_weather_info to show results
    # Ask if user wants to search again
    # Use recursion to search again if user says yes
```

## API Response Structure

The app extracts these details from OpenWeatherMap API response:

```
city name → weather_data["name"]
country → weather_data["sys"]["country"]
temperature → weather_data["main"]["temp"]
description → weather_data["weather"][0]["description"]
humidity → weather_data["main"]["humidity"]
pressure → weather_data["main"]["pressure"]
wind_speed → weather_data["wind"]["speed"]
```

## Challenges I Faced

- **Nested dictionary access** - Getting data from deeply nested JSON (weather[0]["description"])
- **String formatting alignment** - Using f-strings with `:<15` to align output nicely
- **Error handling** - Checking cod != 200 to catch API errors
- **User interruption** - Handling Ctrl+C gracefully with KeyboardInterrupt
- **Recursion for loops** - Using function calling itself instead of while loop for repeat searches
- **Case sensitivity** - Realized city names are case-insensitive (Tokyo, tyoko, TOKYO all work)
- **API key security** - Realized I shouldn't hardcode API key (security risk)

## What Works Well

✓ **Handles typos gracefully** - "Tyoko" → "Error: city not found" → Try again
✓ **Multiple searches** - No need to restart app for new city
✓ **Clean output** - Formatted table that's easy to read
✓ **Error messages** - Clear feedback when something goes wrong
✓ **User-friendly** - "Thank you" message and graceful exit

## Things I Could Add Later

- Save favorite cities to a file
- Display weather forecast (next 5 days)
- Show sunrise/sunset times
- Temperature unit selection (Celsius/Fahrenheit/Kelvin)
- Store API key in environment variables (security fix)
- Search by coordinates instead of city name
- Display weather icons
- Compare weather in multiple cities
- Weather alerts (rain, snow coming)
- Local weather cache (don't call API repeatedly)

## Why This Matters

This project shows I can:
- ✓ Use external APIs (real programming, not just theory)
- ✓ Work with live data (not hardcoded information)
- ✓ Handle errors professionally (user sees messages, not crashes)
- ✓ Structure code properly (functions doing one job each)
- ✓ Format output nicely (professional-looking)
- ✓ Use recursion for control flow
- ✓ Handle user input carefully (KeyboardInterrupt)

Key learnings:
- Real apps use APIs (most of internet is API calls)
- APIs return JSON (just dictionaries in Python)
- Error handling is crucial (things fail, apps should handle it)
- User experience matters (formatting, messages, graceful exits)
- Code doesn't live in isolation (connects to real world)

This project elevated from "practice coding" to "building real apps that do useful things."

---

## ⚠️ Important Notes

**Security Issue:**
- Current code has API key hardcoded (not ideal for GitHub)
- Should use environment variables instead:

```python
import os
api_key = os.getenv("OPENWEATHER_API_KEY")
```

Then set environment variable:
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

**Better for real projects** but current version works fine for learning.

**Requirements:**
- Python 3.6+
- requests library (`pip install requests`)
- Active internet connection
- Working API key (included in code)

---

## Real Output vs Expected

**Test Case 1: Valid city (London)**
✓ Shows all weather details correctly
✓ Asks to search again
✓ User chooses "y"

**Test Case 2: Typo (Tyoko)**
✓ Shows "Error: city not found"
✓ Allows retry
✓ User corrects to "Tokyo"
✓ Shows weather correctly

**Test Case 3: Exit**
✓ User chooses "n"
✓ App shows thank you message
✓ Exits gracefully

**All cases handled properly!**

---

## Next Steps

Next version could:
- Add environment variables for API key
- Implement caching (don't call API for same city twice)
- Add forecast data
- Make it a web app with Flask
- Deploy to cloud

This app is production-ready for a learning project. Real apps that people use are built like this!

Next: Make it even better with more features 🌍
