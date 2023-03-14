from urllib.parse import quote as url_encode
import requests

list_of_destination = ['Лондон', 'аэропорт Шереметьево', 'Череповец']


def weather_forecasts(result=''):
    for i in list_of_destination:
        url = f"https://wttr.in/{url_encode(i)}?nqMT&lang=ru"  # кодирование URL
        response = requests.get(url)
        response.raise_for_status()
        result += response.text
    return result


if __name__ == "__main__":
    weather_forecasts()
