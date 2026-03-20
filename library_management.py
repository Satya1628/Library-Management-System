import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    total_copies INTEGER NOT NULL,
    available_copies INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Loans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    issue_date TEXT,
    return_date TEXT,
    FOREIGN KEY(book_id) REFERENCES Books(book_id),
    FOREIGN KEY(member_id) REFERENCES Members(member_id)
)
""")

conn.commit()


# Add Book
def add_book(title, author, copies):
    cursor.execute(
        "INSERT INTO Books (title, author, total_copies, available_copies) VALUES (?, ?, ?, ?)",
        (title, author, copies, copies)
    )
    conn.commit()
    print("Book added successfully.")


# Add Member
def add_member(name, email):
    cursor.execute(
        "INSERT INTO Members (name, email) VALUES (?, ?)",
        (name, email)
    )
    conn.commit()
    print("Member added successfully.")


# Issue Book
def issue_book(book_id, member_id):
    cursor.execute("SELECT available_copies FROM Books WHERE book_id = ?", (book_id,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        cursor.execute("""
            INSERT INTO Loans (book_id, member_id, issue_date, return_date)
            VALUES (?, ?, ?, NULL)
        """, (book_id, member_id, datetime.now().strftime("%Y-%m-%d")))

        cursor.execute("""
            UPDATE Books
            SET available_copies = available_copies - 1
            WHERE book_id = ?
        """, (book_id,))

        conn.commit()
        print("Book issued successfully.")
    else:
        print("Book not available.")


# Return Book
def return_book(loan_id):
    cursor.execute("""
        SELECT book_id FROM Loans WHERE loan_id = ? AND return_date IS NULL
    """, (loan_id,))
    result = cursor.fetchone()

    if result:
        book_id = result[0]

        cursor.execute("""
            UPDATE Loans
            SET return_date = ?
            WHERE loan_id = ?
        """, (datetime.now().strftime("%Y-%m-%d"), loan_id))

        cursor.execute("""
            UPDATE Books
            SET available_copies = available_copies + 1
            WHERE book_id = ?
        """, (book_id,))

        conn.commit()
        print("Book returned successfully.")
    else:
        print("Invalid loan ID.")


# Simple CLI
def menu():
    while True:
        print("\n1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_book(input("Title: "), input("Author: "), int(input("Copies: ")))
        elif choice == "2":
            add_member(input("Name: "), input("Email: "))
        elif choice == "3":
            issue_book(int(input("Book ID: ")), int(input("Member ID: ")))
        elif choice == "4":
            return_book(int(input("Loan ID: ")))
        elif choice == "5":
            break
        else:
            print("Invalid option.")

menu()
conn.close()