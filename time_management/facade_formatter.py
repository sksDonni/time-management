class FacadeFormatter:
    def format_row(self, row):
        item_no = f"Item No: {row[0]:<4}"
        date = row[1]
        note = row[2]
        days_to_complete = row[3]
        is_complete = row[4]
        record_type = "Task"
        if days_to_complete == "NA":
            record_type = "Note"
        return f"{item_no} Date: {date}, {record_type}: {note} Days to complete: {days_to_complete} Completed: {is_complete}"
