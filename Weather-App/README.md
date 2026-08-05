# Weather App

A simple command-line weather application that fetches real weather data from OpenWeatherMap API and displays current weather information for any city.

## What It Does

- Takes a city name as input
- Fetches live weather data from OpenWeatherMap API
- Displays temperature, weather description, city, and country
- Handles errors if city is not found or API fails

## Features

- **API Integration** - Uses requests library to fetch data
- **Real weather data** - Gets current conditions from OpenWeatherMap
- **Error handling** - Checks for API errors and displays messages
- **Formatted output** - Displays weather in readable format
- **JSON parsing** - Extracts specific data from API response

## How to Run

**Step 1: Get API Key**
1. Go to https://openweathermap.org/api
2. Sign up for free account
3. Get your API key from dashboard

**Step 2: Set Up Code**
1. Install requests library:
```bash
pip install requests
```

2. Open `weather_app.py`
3. Replace `"YOUR_API_KEY"` with your actual API key

**Step 3: Run It**
```bash
python weather_app.py
```

Then enter a city name and see the weather!

## Example Usage

```
Enter city name: London
Weather in London, GB:
Temperature: 15.5°C
Description: Partly cloudy

Enter city name: Tokyo
Weather in Tokyo, JP:
Temperature: 28.3°C
Description: Clear sky

Invalid city:
Enter city name: XyzCity12345
Error: city not found
```

## What I Learned

- **HTTP requests** - Using requests library to get data from APIs
- **API endpoints** - Understanding base URLs and parameters
- **JSON parsing** - Working with JSON responses and accessing nested data
- **Error handling** - Checking response status codes and handling errors
- **Dictionary access** - Using .get() method and accessing nested dictionaries
- **Working with external services** - Understanding API keys and rate limits
- **API parameters** - Passing city name, API key, units (metric/imperial)
- **Response structure** - Understanding how OpenWeatherMap returns data

## Code Structure

```python
def get_weather_data(city):
    # Build API request
    # Send request to OpenWeatherMap
    # Return JSON response

def display_weather_info(weather_data):
    # Check if response was successful
    # Extract city, country, temperature, description
    # Display formatted output

def main():
    # Get city name from user
    # Call API function
    # Call display function
```

## API Response Example

```json
{
  "coord": {"lon": -0.1257, "lat": 51.5085},
  "weather": [{"id": 803, "main": "Clouds", "description": "Broken clouds"}],
  "main": {"temp": 15.5, "feels_like": 14.8, "humidity": 72},
  "name": "London",
  "sys": {"country": "GB"},
  "cod": 200
}
```

## Challenges I Faced

- **Getting API key** - Had to understand where to find it and how to use it
- **Understanding parameters** - Learning what params to pass (city, appid, units)
- **JSON structure** - Accessing nested data like `weather_data["sys"]["country"]`
- **Error checking** - Figuring out that `cod` != 200 means error
- **API documentation** - Reading OpenWeatherMap docs to understand response format
- **Hardcoding API key** - Realized I shouldn't show real API key in code (security issue)

## Things I Could Add Later

- Save favorite cities
- Show weather forecast (next 5 days)
- Show more details (wind speed, humidity, pressure)
- Temperature unit selection (Celsius/Fahrenheit)
- Store API key securely (environment variables)
- Search by coordinates instead of city name
- Display weather icon
- Compare weather in multiple cities
- Cache results so API isn't called repeatedly

## Why This Matters

This is my first project using an external API! Shows:
- Real apps don't just use local data
- APIs are how programs communicate
- Error handling is crucial
- JSON parsing is essential
- Third-party services are common

Key learnings:
- HTTP requests are simple (just need requests library)
- APIs return JSON (just regular dictionaries in Python)
- Error codes matter (cod 200 = success)
- Documentation matters (had to read OpenWeatherMap docs)

This project connected me to the real world—my code now gets actual live data from the internet!

---

## ⚠️ Important Notes

**Security:**
- Don't commit API keys to GitHub
- Use environment variables or .env file for real projects
- Example:
```python
import os
api_key = os.getenv("WEATHER_API_KEY")
```

**API Limits:**
- Free tier has rate limits (1000 calls/day)
- Don't make too many requests in a loop

**Requirements:**
- Python 3.6+
- requests library (`pip install requests`)
- Active internet connection
- Free OpenWeatherMap API key

## Next: Make it Better

Next time I'll:
- Use environment variables for API key
- Add more weather details
- Implement 5-day forecast
- Cache results
- Add database to save cities

This project taught me that real programming = connecting to the real world!

Next: API key security and environment variables 🔐