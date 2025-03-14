# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней.
# Дополнительно, выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta

def get_future_date(current_day):
    today = datetime.now()
    future_date = today + timedelta(current_day)
    format_date = future_date.strftime('%Y-%m-%d')
    return format_date

if __name__ == '__main__':
    days_1 = -5
    days_2 = 10
    print(f'Через {days_1} дней наступит: {get_future_date(days_1)}')
    print(f'Через {days_2} дней наступит: {get_future_date(days_2)}')
