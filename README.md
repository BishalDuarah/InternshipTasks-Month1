# InternshipTasks-Month1
Month 1 was primarily dedicated to Python Programming Mastery. I solidified my understanding of key topics including Loops, Functions, String Operations, File Handling, and Object-Oriented Programming (OOP), and developed 2-3 mini projects applying these concepts. For the final project, I was tasked with building a Personal Finance Manager.
# Personal Finance Manager (Python - CLI)

A multi-user Personal Finance Manager built in Python as part of my internship, designed to track income, expenses, and generate monthly financial reports.

## Features
- Secure multi-user registration and login (SHA-256 password hashing)
- Add, edit, delete income and expense transactions
- Category-based expense tracking (food, rent, travel, etc.)
- Persistent JSON-based data storage
- Monthly summary reports:
  - Total Income
  - Total Expenses
  - Net Savings
  - Category-wise Spending
- Simple and interactive Command-Line Interface (CLI)

## Technologies Used
- Python
- JSON
- Object-Oriented Programming (OOP)
- File I/O
- Error Handling

## Project Structure
personal_finance_manager/
│
├── main.py # CLI and main program logic
├── auth.py # Authentication system
├── storage.py # JSON-based database operations
├── models.py # User and Transaction classes
├── reports.py # Monthly financial reports
└── data/db.json # Persistent data storage
