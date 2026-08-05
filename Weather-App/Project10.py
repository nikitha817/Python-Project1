import requests
def get_weather_data(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    return response.json()
def display_weather_info(weather_data):
    if weather_data.get("cod") != 200:
        print("Error:", weather_data.get("message"))
        return

    city = weather_data["name"]
    country = weather_data["sys"]["country"]
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]

    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description.capitalize()}")
def main():
    city = input("Enter city name: ")
    weather_data = get_weather_data(city)
    display_weather_info(weather_data)
if __name__ == "__main__":
    main()