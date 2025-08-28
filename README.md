Booklist

Overview
The Book Manager is a Python-based application that allows users to manage their personal book collection. It provides a graphical user interface (GUI) built with tkinter to add, search, sort, and update the status of books in the collection. The program stores book data in a JSON file for persistence.  

Features
- Add Books: Add new books to the collection with details such as title, author, year, rating, and status (read/to-read).
- Search Books: Search for books by title, author, or year.
- Change Book Status: Update the status of a book (e.g., from "to-read" to "read") and assign a rating for read books.
- Sort Books: Sort books by title, author, year, rating, or entry time.
- Customizable Display: Toggle the visibility of book details such as author, year, and rating.
- Persistent Storage: All book data is saved in a books.json file for future use.

Requirements
- Python 3.x
- tkinter (comes pre-installed with Python)
- A JSON file named books.json (created automatically if it doesn't exist)

Installation
1. Clone or download the repository.
2. Ensure Python 3.x is installed on your system.
3. Run the program using the following command:
python main.py

Usage
1. Launch the Program: Run the main.py file to open the Book Manager GUI.
2. Add a Book: Click the "Add new book" button, fill in the details, and save.
3. Search for Books: Use the search bar to find books by title, author, or year.
4. Change Book Status: Click the "Change status" button to update a book's status or rating.
5. Sort Books: Use the "Settings" menu to sort books by various categories.
6. Customize Display: Toggle the visibility of book details (author, year, rating) in the "Settings" menu.

File Structure
- main.py: The main program file containing the application logic.
- books.json: A JSON file used to store book data persistently.

Data Format
Books are stored in the books.json file in the following format:
[
  {
    "title": "Book Title",
    "author": "Author Name",
    "year": "Year",
    "rating": "Rating",
    "status": "read/to_read",
    "entry_time": "Timestamp"
  }
]

Customization
- Colors: The program uses a predefined color scheme for the GUI, which can be modified in the set_colours() function in main.py.
- Sorting: The default sorting behavior can be adjusted in the sort_books() function.

Known Issues
- Ensure valid input for fields like year and rating to avoid errors.
- The program may not handle large datasets efficiently due to its reliance on tkinter.

License
This project is open-source and available under the MIT License.
