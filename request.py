import requests

cities = ['Лондон',
          'аэропорт Шереметьево',
          'Череповец']

payload = {'n': '',
           'q': '',
           'M': '',
           'T': '',
           'lang': 'ru'}


def get_forecasts(weather_forecasts=''):
    for city in cities:
        url = f"https://wttr.in/{city}"  # кодирование URL
        response = requests.get(url, params=payload)
        response.raise_for_status()
        weather_forecasts += response.text
    return weather_forecasts


if __name__ == "__main__":
    print(get_forecasts())
