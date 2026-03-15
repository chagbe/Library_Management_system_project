# transactions.py

from data import books, transactions
from utils import (
    generate_transaction_id,
    get_today_date,
    calculate_due_date,
    calculate_fine,
    print_line,
    format_date
)


def checkout_book():
    print_line()
    print("CHECKOUT BOOK")
    print_line()

    book_id = input("Enter book ID to checkout: ").strip().upper()

    if book_id not in books:
        print("Book not found.")
        return

    book = books[book_id]

    if book["available_copies"] <= 0:
        print("Book is out of stock.")
        return

    borrower_name = input("Enter borrower name: ").strip()

    if not borrower_name:
        print("Borrower name cannot be empty.")
        return

    checkout_date = get_today_date()
    due_date = calculate_due_date(7)

    transaction = {
        "transaction_id": generate_transaction_id(transactions),
        "book_id": book_id,
        "book_title": book["title"],
        "borrower_name": borrower_name,
        "checkout_date": checkout_date,
        "due_date": due_date,
        "return_date": None,
        "fine": 0.0,
        "status": "Borrowed"
    }

    transactions.append(transaction)
    book["available_copies"] -= 1
    book["times_borrowed"] += 1

    print("Checkout successful.")
    print(f"Transaction ID: {transaction['transaction_id']}")
    print(f"Book Title: {book['title']}")
    print(f"Borrower: {borrower_name}")
    print(f"Checkout Date: {format_date(checkout_date)}")
    print(f"Due Date: {format_date(due_date)}")


def return_book():
    print_line()
    print("RETURN BOOK")
    print_line()

    transaction_id = input("Enter transaction ID: ").strip().upper()

    for transaction in transactions:
        if transaction["transaction_id"] == transaction_id:
            if transaction["status"] == "Returned":
                print("This book has already been returned.")
                return

            return_date = get_today_date()
            fine = calculate_fine(transaction["due_date"], return_date)

            transaction["return_date"] = return_date
            transaction["fine"] = fine
            transaction["status"] = "Returned"

            book_id = transaction["book_id"]
            books[book_id]["available_copies"] += 1

            print("Return successful.")
            print(f"Book Title: {transaction['book_title']}")
            print(f"Borrower: {transaction['borrower_name']}")
            print(f"Due Date: {format_date(transaction['due_date'])}")
            print(f"Return Date: {format_date(return_date)}")
            print(f"Fine: {fine:.2f}")
            return

    print("Transaction ID not found.")


def view_borrowed_books():
    print_line()
    print("CURRENTLY BORROWED BOOKS")
    print_line()

    borrowed = [t for t in transactions if t["status"] == "Borrowed"]

    if not borrowed:
        print("No borrowed books found.")
        return

    print(f"{'Trans ID':<10}{'Book ID':<10}{'Title':<25}{'Borrower':<20}{'Due Date':<15}")
    print("-" * 80)

    for transaction in borrowed:
        print(
            f"{transaction['transaction_id']:<10}"
            f"{transaction['book_id']:<10}"
            f"{transaction['book_title'][:24]:<25}"
            f"{transaction['borrower_name'][:19]:<20}"
            f"{format_date(transaction['due_date']):<15}"
        )