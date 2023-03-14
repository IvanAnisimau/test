import requests

cities = ['Лондон',
          'аэропорт Шереметьево',
          'Череповец']

payload = {'option': 'n',
           'option1': 'q',
           'option2': 'M',
           'transparency': 'T',
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
