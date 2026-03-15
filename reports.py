# reports.py

from data import books, transactions
from utils import get_today_date, print_line, format_date


def inventory_report():
    print_line()
    print("INVENTORY REPORT")
    print_line()

    total_titles = len(books)
    total_copies = sum(book["total_copies"] for book in books.values())
    available_copies = sum(book["available_copies"] for book in books.values())
    borrowed_copies = total_copies - available_copies

    print(f"Total Book Titles      : {total_titles}")
    print(f"Total Copies           : {total_copies}")
    print(f"Available Copies       : {available_copies}")
    print(f"Borrowed Copies        : {borrowed_copies}")
    print()

    print(f"{'Book ID':<10}{'Title':<25}{'Available':<15}{'Borrowed Count':<15}")
    print("-" * 65)

    for book_id, details in books.items():
        print(
            f"{book_id:<10}"
            f"{details['title'][:24]:<25}"
            f"{str(details['available_copies']) + '/' + str(details['total_copies']):<15}"
            f"{details['times_borrowed']:<15}"
        )


def overdue_books_report():
    print_line()
    print("OVERDUE BOOKS REPORT")
    print_line()

    today = get_today_date()
    overdue_books = [
        t for t in transactions
        if t["status"] == "Borrowed" and t["due_date"] < today
    ]

    if not overdue_books:
        print("No overdue books.")
        return

    print(f"{'Trans ID':<10}{'Book Title':<25}{'Borrower':<20}{'Due Date':<15}{'Days Late':<10}")
    print("-" * 85)

    for transaction in overdue_books:
        days_late = (today - transaction["due_date"]).days
        print(
            f"{transaction['transaction_id']:<10}"
            f"{transaction['book_title'][:24]:<25}"
            f"{transaction['borrower_name'][:19]:<20}"
            f"{format_date(transaction['due_date']):<15}"
            f"{days_late:<10}"
        )


def popular_books_report():
    print_line()
    print("POPULAR BOOKS REPORT")
    print_line()

    popular_books = [
        (book_id, details)
        for book_id, details in books.items()
        if details["times_borrowed"] > 0
    ]

    if not popular_books:
        print("No books have been borrowed yet.")
        return

    popular_books.sort(key=lambda item: item[1]["times_borrowed"], reverse=True)

    print(f"{'Rank':<8}{'Book ID':<10}{'Title':<30}{'Times Borrowed':<15}")
    print("-" * 65)

    for index, (book_id, details) in enumerate(popular_books, start=1):
        print(
            f"{index:<8}"
            f"{book_id:<10}"
            f"{details['title'][:29]:<30}"
            f"{details['times_borrowed']:<15}"
        )


def transaction_summary():
    print_line()
    print("TRANSACTION SUMMARY REPORT")
    print_line()

    total_transactions = len(transactions)
    total_checkouts = len(transactions)
    total_returns = sum(1 for t in transactions if t["status"] == "Returned")
    active_borrowed = sum(1 for t in transactions if t["status"] == "Borrowed")
    total_fines = sum(t["fine"] for t in transactions)

    print(f"Total Transactions     : {total_transactions}")
    print(f"Total Checkouts        : {total_checkouts}")
    print(f"Total Returns          : {total_returns}")
    print(f"Currently Borrowed     : {active_borrowed}")
    print(f"Total Fines Collected  : {total_fines:.2f}")