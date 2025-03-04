import requests


def all_api_date():
    data = requests.get('http://nekopara.ru/date').json()['message']
    return data
print(all_api_date())
def status_win_time(date):
    day, month, year = date.split('-')
    status = requests.get(f'http://nekopara.ru/date?day={day}&month={month}&year={year}').json()['message']
    rooms_count = status['rooms_count']['data']
    print(status)

status_win_time('2-2-2025')
