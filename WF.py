import requests

def get_lat_lon(api_key, city):
    # Use the Geocoding API to get latitude and longitude for the given city
    geocoding_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(geocoding_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        
        if data["cod"] != 200:
            return None  # City not found
        
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        return lat, lon
    
    except requests.exceptions.RequestException as e:
        return None

def get_weather(api_key, city):
    # Get latitude and longitude
    lat_lon = get_lat_lon(api_key, city)
    if lat_lon is None:
        return {"Error": "City not found or invalid API key."}
    
    lat, lon = lat_lon
    
    # Now use the One Call API to get the weather
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        
        data = response.json()
        
        # Check if there's an error code in the response
        if 'current' not in data:
            return {"Error": "Unable to fetch weather data"}
        
        # Extract weather details
        weather = {
            "City": city,
            "Temperature": data['current']['temp'],
            "Weather": data['current']['weather'][0]['description'],
            "Humidity": data['current']['humidity'],
            "Wind Speed": data['current']['wind_speed'],
            "Pressure": data['current']['pressure'],
            "Visibility": data['current']['visibility'] / 1000  # Convert to kilometers
        }
        return weather

    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")  # Enter city name without quotes
    weather_info = get_weather(api_key, city)
    
    if "Error" in weather_info:
        print(weather_info["Error"])
    else:
        print(f"Weather in {weather_info['City']}:")
        print(f"Temperature: {weather_info['Temperature']}°C")
        print(f"Condition: {weather_info['Weather']}")
        print(f"Humidity: {weather_info['Humidity']}%")
        print(f"Wind Speed: {weather_info['Wind Speed']} m/s")
        print(f"Pressure: {weather_info['Pressure']} hPa")
        print(f"Visibility: {weather_info['Visibility']} km")
