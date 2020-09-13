def format_decorator(format_func, *args):
    def format_wrapper(*args):
        formatted_rows = []
        if args:
            for row in args[0]:
                formatted_rows.append(format_func(row))
        return formatted_rows

    return format_wrapper


@format_decorator
def format_task(row):
    item = f"Item: {row[0]:<4}"
    event_type = f"{row[1]}"
    task = f"{row[2]:<100}"
    date_set = f"Date: {row[3]}"
    days_to_complete = f"Days to complete: {row[5]}"
    is_complete = f"Completed: {row[6]:<5}"
    return f"{item} {date_set} {event_type}: {task} [{days_to_complete}, {is_complete}]"


@format_decorator
def format_note(row):
    item = f"Item: {row[0]:<4}"
    event_type = f"{row[1]}"
    note = f"{row[2]}"
    date_set = f"Date: {row[3]}"
    return f"{item} {date_set} {event_type}: {note}"
