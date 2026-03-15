# inventory.py

from data import books
from utils import generate_book_id, validate_positive_integer, print_line


def add_book():
    print_line()
    print("ADD NEW BOOK")
    print_line()

    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    genre = input("Enter genre: ").strip()
    total_copies_input = input("Enter total copies: ").strip()

    total_copies = validate_positive_integer(total_copies_input)

    if not title or not author or not genre:
        print("Error: Title, author, and genre cannot be empty.")
        return

    if total_copies is None:
        print("Error: Total copies must be a positive integer.")
        return

    book_id = generate_book_id(books)
    books[book_id] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies,
        "times_borrowed": 0
    }

    print(f"Book added successfully. Book ID: {book_id}")


def update_book():
    print_line()
    print("UPDATE BOOK")
    print_line()

    book_id = input("Enter book ID to update: ").strip().upper()

    if book_id not in books:
        print("Book ID not found.")
        return

    book = books[book_id]

    print("Leave blank if you do not want to change a field.")
    new_title = input(f"Enter new title [{book['title']}]: ").strip()
    new_author = input(f"Enter new author [{book['author']}]: ").strip()
    new_genre = input(f"Enter new genre [{book['genre']}]: ").strip()
    new_total_copies_input = input(f"Enter new total copies [{book['total_copies']}]: ").strip()

    if new_title:
        book["title"] = new_title

    if new_author:
        book["author"] = new_author

    if new_genre:
        book["genre"] = new_genre

    if new_total_copies_input:
        new_total_copies = validate_positive_integer(new_total_copies_input)
        if new_total_copies is None:
            print("Invalid total copies. Update cancelled.")
            return

        borrowed_count = book["total_copies"] - book["available_copies"]
        if new_total_copies < borrowed_count:
            print("Error: New total copies cannot be less than borrowed copies.")
            return

        book["total_copies"] = new_total_copies
        book["available_copies"] = new_total_copies - borrowed_count

    print("Book updated successfully.")


def view_books():
    print_line()
    print("BOOK INVENTORY")
    print_line()

    if not books:
        print("No books available.")
        return

    print(f"{'ID':<8}{'Title':<25}{'Author':<20}{'Genre':<18}{'Available':<10}{'Borrowed':<10}")
    print("-" * 95)

    for book_id, details in books.items():
        print(
            f"{book_id:<8}"
            f"{details['title'][:24]:<25}"
            f"{details['author'][:19]:<20}"
            f"{details['genre'][:17]:<18}"
            f"{details['available_copies']}/{details['total_copies']:<10}"
            f"{details['times_borrowed']:<10}"
        )


def search_book():
    print_line()
    print("SEARCH BOOK")
    print_line()

    keyword = input("Enter title, author, or genre: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found_books = []

    for book_id, details in books.items():
        if (
            keyword in details["title"].lower()
            or keyword in details["author"].lower()
            or keyword in details["genre"].lower()
        ):
            found_books.append((book_id, details))

    if not found_books:
        print("No matching books found.")
        return

    print(f"{'ID':<8}{'Title':<25}{'Author':<20}{'Genre':<18}{'Available':<10}")
    print("-" * 85)

    for book_id, details in found_books:
        print(
            f"{book_id:<8}"
            f"{details['title'][:24]:<25}"
            f"{details['author'][:19]:<20}"
            f"{details['genre'][:17]:<18}"
            f"{details['available_copies']}/{details['total_copies']:<10}"
        )