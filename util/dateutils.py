import datetime


def get_formatted_date() -> str:
    return datetime.datetime.now().strftime('%d-%b')