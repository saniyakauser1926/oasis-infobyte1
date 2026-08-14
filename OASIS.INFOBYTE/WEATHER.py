import requests

API_KEY = "76c05111105f20537757e423688d3b1f"
BASE_URL = ("https://api.openweathermap.org/data/2.5/weather")

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if data.get("cod") != 200:
            print(f"Error: {data.get('message', 'City not found').capitalize()}\n")
            return

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9/5) + 32
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp_c:.1f}°C / {temp_f:.1f}°F")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.\n")
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.\n")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n")


def main():
    print("=== Weather App ===\n")
    while True:
        city = input("Enter city name (or 'quit'): ").strip()
        if city.lower() == "quit":
            break
        if city == "":
            print("Error: City cannot be empty.\n")
            continue
        get_weather(city)


if __name__ == "__main__":
    main()