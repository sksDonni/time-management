from datetime import datetime
from datetime import timedelta

string_format_time = "%Y-%m-%d %H:%M:%S"


def get_date_time():
    return datetime.now().strftime(string_format_time)


def is_overdue(date_time, completion_goal):
    dt = datetime.strptime(date_time, string_format_time)
    completion_goal = float(completion_goal)
    return (dt + timedelta(days=completion_goal)) < datetime.now()
