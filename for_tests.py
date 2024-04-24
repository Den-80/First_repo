from datetime import datetime

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def string_to_date(date_string: str):
    formatted_datetime = datetime.strptime(date_string, "%Y.%m.%d")
    converted_date = datetime.date(formatted_datetime)
    return converted_date


def date_to_string(date):
    date_string = date.strftime('%Y.%m.%d')
    return date_string


def get_upcoming_birthdays(list_users: list) -> list: 
    for user in users:
        user_name = user.get('name')
        user_birthday = user.get('birthday')
        user_birthday_datetime = string_to_date(user_birthday)
        if user_birthday_datetime in 