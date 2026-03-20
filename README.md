# Library Management System (Python & SQLite)

This is a Command Line Interface (CLI) based Library Management System developed using Python and SQLite. The system allows users to manage books, members, and borrowing records while maintaining data integrity through a relational database.

The project demonstrates core database operations, structured programming, and basic system design principles.

---

## Features

- Add new books to the library
- Register new members
- Issue books to members
- Return books and update availability
- Maintain loan records with issue and return dates
- Uses relational database with foreign key constraints

---

## Tech Stack

- Python
- SQLite (Database)
- SQL (Queries and Data Management)

---

## Database Schema

### Books Table
- book_id (Primary Key)
- title
- author
- total_copies
- available_copies

### Members Table
- member_id (Primary Key)
- name
- email (Unique)

### Loans Table
- loan_id (Primary Key)
- book_id (Foreign Key)
- member_id (Foreign Key)
- issue_date
- return_date

---

## How It Works

1. The system connects to an SQLite database (`library.db`)
2. Tables are created automatically if they do not exist
3. Users can:
   - Add books and members
   - Issue books (reduces available copies)
   - Return books (updates availability)
4. Loan records track borrowing history

---

## How to Run

1. Make sure Python is installed
2. Download or clone the repository
3. Run the program:

```bash
python library_management.py
```

4. Use the menu options to interact with the system

---

## Project Structure

```
Library-Management-System/
│
├── library_management.py
├── library.db (auto-created)
├── README.md
```

---

## Concepts Used

- Relational Database Design
- CRUD Operations
- SQL Joins and Constraints
- Data Integrity (Primary & Foreign Keys)
- CLI-based Application Design

---

## Future Improvements

- Add search functionality (by book or member)
- Add overdue tracking and fine calculation
- Build GUI using Tkinter or Web Interface
- Add reporting (most borrowed books, active users)

---

## Author

**T Satyanarayana Reddy**  
B.Tech CSE (Data Science)  
Lovely Professional University
