from datetime import datetime, timedelta

def generate_book_id(books):
    return f"B{len(books) + 1:03}"

def generate_transaction_id(transactions):
    return f"T{len(transactions) + 1:03}"

def get_today_date():
    return datetime.today().date()

def calculate_due_date(days=7):
    return get_today_date() + timedelta(days=days)

def calculate_fine(due_date, return_date, fine_per_day=1.0):
    overdue_days = (return_date - due_date).days
    if overdue_days > 0:
        return overdue_days * fine_per_day
    return 0.0

def validate_positive_integer(value):
    try:
        number = int(value)
        if number > 0:
            return number
        return None
    except ValueError:
        return None

def print_line(length=60):
    print("=" * length)

def format_date(date_value):
    if date_value is None:
        return "Not Returned"
    return date_value.strftime("%Y-%m-%d")