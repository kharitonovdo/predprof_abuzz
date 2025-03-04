import requests


def all_api_date():
    data = requests.get('http://nekopara.ru/date').json()['message']
    return data