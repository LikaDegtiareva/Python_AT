# Напишите скрипт, который получает текущее время и дату, а затем выводит их в формате YYYY-MM-DD HH:MM:SS.
# Дополнительно, выведите день недели и номер недели в году.

from datetime import datetime

def get_naw_datetime():
    today = datetime.now()

    format_date = today.strftime('%Y-%m-%d %H:%M:%S')
    print(f'Текущая дата и время: {format_date}')

    day_of_week = today.strftime('%A')
    print(f'День недели: {day_of_week}')

    week_number = today.isocalendar().week
    print(f'Номер недели в текущем году: {week_number}')

if __name__ == '__main__':
    get_naw_datetime()