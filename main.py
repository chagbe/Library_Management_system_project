from inventory import add_book, update_book, view_books, search_book
from transactions import checkout_book, return_book, view_borrowed_books
from reports import inventory_report, overdue_books_report, popular_books_report, transaction_summary

def inventory_menu():
    while True:
        print("\n=== INVENTORY MANAGEMENT ===")
        print("1. Add New Book")
        print("2. Update Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            view_books()
        elif choice == "4":
            search_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

def transaction_menu():
    while True:
        print("\n=== TRANSACTION MANAGEMENT ===")
        print("1. Checkout Book")
        print("2. Return Book")
        print("3. View Borrowed Books")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            checkout_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            view_borrowed_books()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def report_menu():
    while True:
        print("\n=== REPORTS ===")
        print("1. Inventory Report")
        print("2. Overdue Books Report")
        print("3. Popular Books Report")
        print("4. Transaction Summary")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory_report()
        elif choice == "2":
            overdue_books_report()
        elif choice == "3":
            popular_books_report()
        elif choice == "4":
            transaction_summary()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        print("\n=== LIBRARY MANAGER SYSTEM ===")
        print("1. Inventory Management")
        print("2. Transaction Management")
        print("3. Reports")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory_menu()
        elif choice == "2":
            transaction_menu()
        elif choice == "3":
            report_menu()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()