import requests

class WeatherService:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        self._base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city_name: str) -> tuple[str, float] | None:
        params = {
            "q": city_name,
            "appid": self._api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self._base_url, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(f"Weather request failed: {error}")
            return None

        data = response.json()

        try:
            weather_description = data["weather"][0]["description"]
            temperature_celsius = data["main"]["temp"]
            return weather_description, temperature_celsius
        except (KeyError, IndexError, TypeError):
            print("Failed to parse weather data.")
            return None

class WeatherApp:
    def __init__(self, weather_service: WeatherService) -> None:
        self._weather_service = weather_service

    def run(self) -> None:
        city_name = input("Enter city name: ").strip()

        if not city_name:
            print("City name was not provided.")
            return

        weather = self._weather_service.get_weather_by_city(city_name)

        if weather is None:
            return

        weather_description, temperature_celsius = weather
        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature_celsius:.1f} °C")

def main() -> None:
    api_key = "179a98afdd3822bc50c6117f4a42a117" # Oh no, I just leaked my API key. If someone is reading this, please, do not use it.

    weather_service = WeatherService(api_key)
    app = WeatherApp(weather_service)
    app.run()

main()