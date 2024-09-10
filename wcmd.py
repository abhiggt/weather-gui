# climate_detector.py

import requests

def get_weather(city, api_key):
    # OpenWeatherMap API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Full URL with city and API key
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

    # Send request to the API
    response = requests.get(complete_url)

    # Convert the response to JSON format
    weather_data = response.json()

    # Check if the city is found
    if weather_data['cod'] == 200:
        # Extract main data
        main = weather_data['main']
        weather = weather_data['weather'][0]

        # Display weather details
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
    else:
        print("City not found, please try again.")

if __name__ == "__main__":
    # Replace with your actual OpenWeatherMap API key
    api_key = "8568da25818157d76051c7f5142f771b"
    
    # Input the city name
    city = input("Enter city name: ")

    # Fetch and display the weather details
    get_weather(city, api_key)
