import requests


def all_api_date():
    data = requests.get('http://nekopara.ru/date').json()['message']
    return data

def status_win_time(date):
    day, month, year = date.split('-')
    status = requests.get(f'http://nekopara.ru/date?day={day}&month={month}&year={year}').json()['message']
    rooms_count = status['rooms_count']['data']
    potok_statusov = status['windows']['data']
    matrix = []

    for level in range(1, len(potok_statusov) + 1):
        matrix += [list(map(int, potok_statusov[f'floor_{level}']))]
    return matrix
