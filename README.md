video:https://drive.google.com/file/d/1WN8Xb8uWq_6wAt0TAYvVc35ApzwStQBK/view?usp=drivesdk
Personal Journal Manager

📌 Project Overview

The Personal Journal Manager is a simple Python-based console application that allows users to maintain a personal journal using a text file.

The program provides options to:

- Add new journal entries
- View all saved entries
- Search for entries using a keyword or date
- Delete all journal entries
- Exit the application

Each journal entry is automatically saved with the date and time when it was created.

---

🎯 Objectives

The main objectives of this project are:

- To practice Object-Oriented Programming (OOP) in Python.
- To understand file handling in Python.
- To work with date and time using the "datetime" module.
- To implement a menu-driven program.
- To handle errors using exception handling.
- To create, read, append, search, and modify data stored in a text file.

---

🛠️ Technologies Used

- Programming Language: Python
- Module Used: "datetime"
- Storage: Text file ("journal.txt")
- Concepts: OOP, File Handling, Loops, Conditional Statements, Exception Handling

---

✨ Features

1. Add a New Entry

The user can enter a journal entry, which is stored in "journal.txt".

Each entry contains:

- Date
- Time
- Journal text
- Separator line

Example:

[2026-10-02 14:25:30]
Today was a productive day.
------------------------------

---

2. View All Entries

This option reads the "journal.txt" file and displays all saved journal entries.

If there are no entries, the program displays an appropriate message.

---

3. Search for an Entry

Users can search for an entry using:

- A keyword
- A date
- Any text contained in the entry

The program checks the saved journal data and displays matching information.

Example:

Enter a keyword or date to search: college

Matching Entries:
----------------------------------------
[2026-10-02 14:25:30]
Today I went to college.

---

4. Delete All Entries

The user can delete all journal entries after confirmation.

The program asks:

Are you sure you want to delete all entries? (yes/no):

If the user enters "yes", all existing journal data is removed.

---

5. Exit

The user can select option "5" to safely exit the program.

---

📂 File Structure

Personal-Journal-Manager/
│
├── journal.py
├── journal.txt
└── README.md

"journal.py"

Contains the complete Python program.

"journal.txt"

Stores all journal entries created by the user. It is automatically created when the first entry is added.

"README.md"

Contains the documentation and information about the project.

---

🧠 Concepts Used

Object-Oriented Programming

A class named "journalmanager" is created to organize the journal operations.

class journalmanager:

An object of the class is then created:

journal = journalmanager()

---

Constructor

The "__init__()" method initializes the filename used for storing journal entries.

def __init__(self):
    self.filename = "journal.txt"

---

File Handling

The program uses Python's "open()" function to work with the journal file.

Different file modes are used:

- ""x"" → Creates a new file
- ""a"" → Adds new content to the file
- ""r"" → Reads the file
- ""w"" → Clears/replaces the file contents

---

Date and Time

The "datetime" module is used to record when an entry was created.

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

---

Exception Handling

"try-except" blocks are used to handle possible errors such as:

- File not found
- Invalid menu input
- File already existing

Example:

try:
    choice = int(input("\nUser Input: "))
except ValueError:
    print("\nInvalid option. Please select from the menu.")

---

🔄 Program Flow

Start
  ↓
Display Menu
  ↓
Choose an Option
  ↓
 ┌─────────────────────────────┐
 │ 1. Add Entry                │
 │ 2. View Entries             │
 │ 3. Search Entry             │
 │ 4. Delete Entries           │
 │ 5. Exit                     │
 └─────────────────────────────┘
  ↓
Perform Selected Operation
  ↓
Return to Menu
  ↓
Exit when Option 5 is Selected

---

▶️ How to Run

Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

python --version

Step 2: Save the Program

Save the code in a Python file, for example:

journal.py

Step 3: Run the Program

Open the terminal in the project folder and run:

python journal.py

Step 4: Use the Menu

The program will display:

Welcome to Personal Journal Manager!

Please select an option:
1. Add a new Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter the number corresponding to the operation you want to perform.

---

📋 Sample Output

Welcome to Personal Journal Manager!

Please select an option:
1. Add a new Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 1

Enter your journal entry: Today I completed my Python project.

Entry added successfully!

Viewing the entries:

Your journal entries:
----------------------------------------
[2026-10-02 14:25:30]
Today I completed my Python project.
------------------------------

---

⚠️ Error Handling

The program handles several common errors:

Error| Handling
Invalid menu input| "ValueError"
Journal file doesn't exist| "FileNotFoundError"
Journal file already exists| "FileExistsError"
Empty journal| Displays an appropriate message

---

🚀 Future Improvements

The project can be improved by adding:

- Edit/update existing entries
- Delete a single entry instead of all entries
- Password protection
- Better search functionality
- Categories or tags for entries
- Separate journal files for different users
- A graphical user interface (GUI)
- Database storage instead of a text file

---

📚 Learning Outcomes

After completing this project, the user can understand:

- How classes and objects work in Python
- How to create and use methods
- How to read and write files
- How to append data to a file
- How to search text inside a file
- How to use "datetime"
- How to use "try-except"
- How to build a menu-driven Python application

---

👨‍💻 Author

Personal Journal Manager Project

Developed using Python as a practice project for learning Object-Oriented Programming and File Handling.
