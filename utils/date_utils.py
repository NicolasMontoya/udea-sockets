from datetime import datetime, timedelta


def add_hours(number_of_hours):
    return datetime.now() + timedelta(hours=number_of_hours)