import requests

API_KEY = '8f3e86f89fdbb70120c80bc243d65e8b'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f'{BASE_URL}?q={city}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp'] - 273.15
        return f'The weather in {city} is {weather} and the temperature is {temp:.2f} Celsius'
        
    else:
        print(response, response.status_code)
        return None
    

if __name__ == '__main__':
    city = input('Enter the city name: ')
    print(get_weather(city))
    