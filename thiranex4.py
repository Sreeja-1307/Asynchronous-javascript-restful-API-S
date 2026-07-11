import asyncio
import aiohttp

API_KEY = "YOUR_API_KEY"   # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

async def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(BASE_URL, params=params) as response:

                if response.status == 404:
                    print("City not found.")
                    return

                if response.status != 200:
                    print("Error:", response.status)
                    return

                data = await response.json()

                print("\n===== Weather Dashboard =====")
                print(f"City        : {data['name']}")
                print(f"Country     : {data['sys']['country']}")
                print(f"Temperature : {data['main']['temp']} °C")
                print(f"Humidity    : {data['main']['humidity']}%")
                print(f"Wind Speed  : {data['wind']['speed']} m/s")
                print(f"Pressure    : {data['main']['pressure']} hPa")
                print(f"Weather     : {data['weather'][0]['description'].title()}")

        except aiohttp.ClientConnectionError:
            print("Network connection error.")
        except asyncio.TimeoutError:
            print("Request timed out.")
        except Exception as e:
            print("Unexpected error:", e)

async def main():
    city = input("Enter city name: ")
    await fetch_weather(city)

if __name__ == "__main__":
    asyncio.run(main())