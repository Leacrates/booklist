import json
import tkinter as tk
import time
from datetime import datetime


class Book:
    def __init__(self, title, author, year, rating, status, entry_time):
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating
        self.status = status
        self.entry_time = entry_time

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "rating": self.rating,
            "status": self.status,
            "entry_time": self.entry_time
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["year"], data["rating"], data["status"], data["entry_time"])


def set_colours():
    black = "#000000"
    dark_beige = "#804F10"
    beige = "#DBC5B0"
    dark_red = "#9B483E"
    red = "#BD7F77"
    light_red = "#DCB4AF"
    dark_green = "#588629"
    green = "#8EAB6F"
    light_green = "#B4CF97"
    light_beige = "#F2EADA"

    colour1_v = dark_beige  # headline banner
    colour2_v = light_beige  # background
    colour3_v = dark_red  # to read category
    colour4_v = red  # read subcategories
    colour5_v = light_red  # read content
    colour6_v = dark_green  # to read category
    colour7_v = green  # to read subcategories
    colour8_v = light_green  # to read content
    colour9_v = beige  # buttons

    colour1_text_v = light_beige
    colour2_text_v = black
    colour3_text_v = light_beige
    colour4_text_v = light_beige
    colour5_text_v = black
    colour6_text_v = light_beige
    colour7_text_v = light_beige
    colour8_text_v = black
    colour9_text_v = black

    return (colour1_v, colour2_v, colour3_v, colour4_v, colour5_v, colour6_v, colour7_v, colour8_v, colour9_v,
            colour1_text_v, colour2_text_v, colour3_text_v, colour4_text_v, colour5_text_v, colour6_text_v,
            colour7_text_v, colour8_text_v, colour9_text_v)


def save_data(data):
    book_list = [book_v.to_dict() for book_v in data]
    with open("books.json", "w") as file:
        json.dump(book_list, file)


def load_data():
    try:
        with open("books.json", "r") as file:
            books_list = json.load(file)
            return [Book.from_dict(book_v) for book_v in books_list]
    except FileNotFoundError:
        print("No data file found. Starting with an empty book list.")
        return []


def refresh_books(window_v):
    # Clear all widgets in the book display area
    for widget in window_v.grid_slaves():
        if int(widget.grid_info()["row"]) >= 2:  # Rows 3 and below are for books
            widget.destroy()
    time.sleep(0.1)  # Small delay to ensure widgets are cleared before redrawing
    (start_category_to_read_v, show_author_v, show_year_v, show_rating_v, column_for_author_v, column_for_year_v,
     column_for_rating_v) = set_categories(show_author, show_year, show_rating)
#    print(column_for_author_v, column_for_year_v, column_for_rating_v)
#    display_everything(window_v)
    return (start_category_to_read_v, show_author_v, show_year_v, show_rating_v,
            column_for_author_v, column_for_year_v, column_for_rating_v)


def window_add_book(window):
    window2 = tk.Tk()
    window2.title("Add Book")
    window2.geometry("500x500")
    window2.minsize(500, 500)
    window2.maxsize(500, 500)
    window2.configure(bg=colour2)

    def toggle_switch(switch_var):
        if switch_var.get():
            switch_var.set(False)
            entry_status.configure(text="to read")
        else:
            switch_var.set(True)
            entry_status.configure(text="read")

    headline2 = tk.Label(window2, text="Add Book", height=1, bg=colour1, fg=colour1_text, font=("Arial", 25, "bold"))
    headline2.grid(row=0, column=0, columnspan=20, pady=20, sticky="nsew")

    # Labels for book details
    title_label = tk.Label(window2, text="Title:", bg=colour2, fg=colour2_text, font=("Arial", 16, "bold"))
    author_label = tk.Label(window2, text="Author:", bg=colour2, fg=colour2_text, font=("Arial", 16, "bold"))
    year_label = tk.Label(window2, text="Year:", bg=colour2, fg=colour2_text, font=("Arial", 16, "bold"))
    rating_label = tk.Label(window2, text="Rating:", bg=colour2, fg=colour2_text, font=("Arial", 16, "bold"))
    status_label = tk.Label(window2, text="Status:", bg=colour2, fg=colour2_text, font=("Arial", 16, "bold"))

    title_label.grid(row=1, column=0, pady=5, padx=15)
    author_label.grid(row=2, column=0, pady=5, padx=15)
    year_label.grid(row=3, column=0, pady=5, padx=15)
    rating_label.grid(row=4, column=0, pady=5, padx=15)
    status_label.grid(row=5, column=0, pady=5, padx=15)

    # Entry fields for book details
    switch_state_status = tk.BooleanVar(value=True)  # Default status is "to_read"
    entry_title = tk.Entry(window2, bg=colour9, fg=colour9_text, width=30, font=("Arial", 16))
    entry_author = tk.Entry(window2, width=30, bg=colour9, fg=colour9_text, font=("Arial", 16))
    entry_year = tk.Entry(window2, width=30, bg=colour9, fg=colour9_text, font=("Arial", 16))
    entry_rating = tk.Entry(window2, width=30, bg=colour9, fg=colour9_text, font=("Arial", 16))
    entry_status = tk.Checkbutton(window2, width=30, text="read", onvalue=True, offvalue=False,
                                  indicatoron=False, font=("Arial", 16), variable=switch_state_status,
                                  command=lambda: toggle_switch(switch_state_status))
    entry_status.configure(bg=colour9, fg=colour9_text, activebackground=colour9, activeforeground=colour9_text,
                           selectcolor=colour9)

    entry_title.grid(row=1, column=1, pady=10)
    entry_author.grid(row=2, column=1, pady=10)
    entry_year.grid(row=3, column=1, pady=10)
    entry_rating.grid(row=4, column=1, pady=10)
    entry_status.grid(row=5, column=1, pady=10)

    def save_book():

        def set_error_box(text):
            error_box = tk.Label(window2, text=text, bg=colour3, fg=colour3_text, width=30, height=1,
                                 font=("Arial", 16, "bold"))
            error_box.grid(row=6, column=0, columnspan=2, pady=10)

        if not entry_title.get() or not entry_author.get() or not entry_year.get():
            set_error_box("All fields are required!")
            print("Error", "All fields are required!")
            return
        if switch_state_status.get() is not True and switch_state_status.get() is not False:
            set_error_box("Status must be 'read' or 'to_read'!")
            print("Error")
            return
        if entry_year.get().isdigit() is False or int(entry_year.get()) < 0:
            set_error_box("Year must be a positive integer!")
            print("Error", "Year must be a positive integer!")
            return
        if entry_rating.get() != "" and entry_status != "to_read":
            if entry_rating.get().isdigit() is False:
                set_error_box("Rating must be integer!")
                print("Error", "Year must be integer!")
                return
        if entry_rating.get() == "" and switch_state_status.get() is not False:
            set_error_box("Rating is required for read books!")
            print("Error", "Rating is required for read books!")
            return

        title = entry_title.get()
        author = entry_author.get()
        year = entry_year.get()
        rating = entry_rating.get()
        if rating == "":
            rating = "?"
        status = switch_state_status.get()
        if status:
            status = "read"
        else:
            status = "to_read"
        entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        book_v1 = Book(title, author, year, rating, status, entry_time)
        all_books.append(book_v1)
        save_data(all_books)
        (start_category_to_read_v, show_author_v, show_year_v, show_rating_v, column_for_author_v, column_for_year_v,
         column_for_rating_v) = refresh_books(window)
        display_everything(window, column_for_author_v, column_for_year_v, column_for_rating_v)
        window2.destroy()

    window2.grid_rowconfigure(6, weight=1)
    window2.grid_rowconfigure(7, weight=0)
    window2.grid_columnconfigure(0, weight=1)
    window2.grid_columnconfigure(1, weight=1)

    # Button to save the book
    save_button = tk.Button(window2, text="Save Book", command=save_book, width=30, height=2, bg=colour9,
                            fg=colour9_text, font=("Arial", 16, "bold"))
    save_button.grid(row=7, column=0, columnspan=2, pady=20, sticky="s")
    save_button.configure(bg=colour9, fg=colour9_text, activebackground=colour1, activeforeground=colour1_text)


def window_status_change(window_v):
    window_status = tk.Toplevel()

    def window_status_change_settings():
        window_status.title("Change Book Status")
        window_status.geometry("500x500")
        window_status.minsize(500, 500)
        window_status.configure(bg=colour2)

        window_status.grid_columnconfigure(0, weight=1)

        headline_status = tk.Label(window_status, text="Change Book Status", height=1, bg=colour1, fg=colour1_text,
                                   font=("Arial", 25, "bold"))
        headline_status.grid(row=0, column=0, columnspan=20, pady=20, sticky="nsew")

    def change_status_confirm(book, window_check, rating_var, new_rarting_window_v):
        new_rarting_window_v.destroy()
        # Check if the rating is an integer
        try:
            rating_var = int(rating_var.get())
        except ValueError:
            print("Error", "Rating must be an integer!")

            new_rating(book, window_check)
            return

        # Change the status of the book
        if book.status == "to_read":
            book.status = "read"
            book.rating = rating_var
        else:
            book.status = "to_read"
            book.rating = "?"

        save_data(all_books)
        window_status.destroy()
        refresh_books(window_v)
        display_everything(window_v, column_for_author, column_for_year, column_for_rating)

    def new_rating(book, window_check):
        new_rating_window = tk.Toplevel()

        new_rating_window.configure(bg=colour2)
        new_rating_window.grid_columnconfigure(0, weight=1)

        if book.status == "to_read":
            new_rating_window.title("Rate " + book.title)
            new_rating_window.geometry("800x300")
            headline_new_rating = tk.Label(new_rating_window, text=f"How would you rate '{book.title}'?", bg=colour1,
                                           fg=colour1_text, font=("Arial", 20, "bold"))
            headline_new_rating.grid(row=0, column=0, columnspan=20, pady=20, sticky="nsew")

            entry_new_rating_var = tk.StringVar()
            entry_new_rating = tk.Entry(new_rating_window, bg=colour9, fg=colour9_text, font=("Arial", 16),
                                        textvariable=entry_new_rating_var)
            entry_new_rating.grid(row=1, column=0, columnspan=20, pady=20, padx=10, sticky="nsew")

            confirm_rating_button = tk.Button(new_rating_window, text="Confirm Rating", width=20, height=2, bg=colour6,
                                              fg=colour6_text, activeforeground=colour7_text,
                                              activebackground=colour7, font=("Arial", 20, "bold"),

                                              command=lambda: change_status_confirm(book, window_check,
                                                                                    entry_new_rating_var,
                                                                                    new_rating_window))
            confirm_rating_button.grid(row=2, column=0, columnspan=20, pady=20, padx=80, sticky="nsew")
        else:
            new_rating_window.title("Change status of" + book.title)
            new_rating_window.geometry("1000x300")
            headline_confirm_status = tk.Label(new_rating_window,
                                               text=f"Do you want to change the status of '{book.title}'?", bg=colour1,
                                               fg=colour1_text, font=("Arial", 20, "bold"))
            headline_confirm_status.grid(row=0, column=0, columnspan=20, pady=20, sticky="nsew")
            entry_new_rating_var = tk.StringVar()
            entry_new_rating_var.set(str(3))  # Set the current rating as default
            confirm_change_status_button = tk.Button(new_rating_window, text="Confirm Status Change", width=20,
                                                     height=2, bg=colour6, fg=colour6_text,
                                                     activeforeground=colour7_text, activebackground=colour7,
                                                     font=("Arial", 20, "bold"),
                                                     command=lambda: change_status_confirm(book, window_check,
                                                                                           entry_new_rating_var,
                                                                                           new_rating_window))
            confirm_change_status_button.grid(row=1, column=0, columnspan=20, pady=20, padx=80, sticky="nsew")

    def display_search_results(found_books_v):
        # Clear previous search results
        colour_books_search = colour7
        colour_books = colour7_text
        active_colour_books_search = colour8
        active_colour_books = colour8_text
        for widget in window_status.grid_slaves():
            if int(widget.grid_info()["row"]) >= 3:
                widget.destroy()

        if not found_books_v:
            error_label = tk.Label(window_status, text="No matching books found.", bg=colour3, fg=colour3_text,
                                   font=("Arial", 16, "bold"))
            error_label.grid(row=3, column=0, columnspan=1, pady=20, padx=10, sticky="nsew")
            return

        for idx, found_book in enumerate(found_books_v):
            found_book_label_title = tk.Button(window_status, text=f"{found_book.title}",
                                               command=lambda b=found_book: new_rating(b, window_status),
                                               bg=colour_books_search, fg=colour_books,
                                               activebackground=active_colour_books_search,
                                               activeforeground=active_colour_books, font=("Arial", 16, "bold"))
            found_book_label_title.grid(row=3 + idx, column=0, columnspan=1, pady=20, padx=10, sticky="nsew")

    def search_books(*args):
        search_term = search_var.get().strip().lower()
        if not search_term:
            display_search_results([])
            return

        found_books = [
            book for book in all_books
            if (search_term in book.title.lower())
        ]
        display_search_results(found_books)

    # Search field with StringVar
    search_var = tk.StringVar()
    search_var.trace("w", search_books)  # Call search_books on any change
    entry_search_field = tk.Entry(window_status, textvariable=search_var, bg=colour9, fg=colour9_text,
                                  font=("Arial", 16))
    entry_search_field.grid(row=1, column=0, columnspan=1, pady=20, padx=10, sticky="nsew")

    # Initial empty search results
    display_search_results([])

    window_status_change_settings()


def window_search_books():

    def settings_search():
        headline_search = tk.Label(window_search, text="Search for books", height=1, bg=colour1, fg=colour1_text,
                                   font=("Arial", 25, "bold"))
        headline_search.grid(row=0, column=0, columnspan=20, pady=20, sticky="nsew")

        colour_headlines = colour6
        colour_headlines_text = colour6_text

        title_headline = tk.Label(window_search, text="Title", bg=colour_headlines, fg=colour_headlines_text,
                                  font=("Arial", 16, "bold"))
        author_headline = tk.Label(window_search, text="Author", bg=colour_headlines, fg=colour_headlines_text,
                                   font=("Arial", 16, "bold"))
        year_headline = tk.Label(window_search, text="Year", bg=colour_headlines, fg=colour_headlines_text,
                                 font=("Arial", 16, "bold"))
        rating_headline = tk.Label(window_search, text="Rating", bg=colour_headlines, fg=colour_headlines_text,
                                   font=("Arial", 16, "bold"))

        title_headline.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        author_headline.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        year_headline.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        rating_headline.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

    def display_search_results(found_books_v):
        # Clear previous search results
        colour_books_search = colour8
        colour_books = colour8_text
        for widget in window_search.grid_slaves():
            if int(widget.grid_info()["row"]) >= 3:
                widget.destroy()

        if not found_books_v:
            error_label = tk.Label(window_search, text="No matching books found.", bg=colour3, fg=colour3_text,
                                   font=("Arial", 16, "bold"))
            error_label.grid(row=3, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")
            return

        for idx, found_book in enumerate(found_books_v):
            found_book_label_title = tk.Label(window_search, text=f"{found_book.title}",
                                              bg=colour_books_search, fg=colour_books, font=("Arial", 16, "bold"))
            found_book_label_author = tk.Label(window_search, text=f"{found_book.author}",
                                               bg=colour_books_search, fg=colour_books, font=("Arial", 16, "bold"))
            found_book_label_year = tk.Label(window_search, text=f"{found_book.year}",
                                             bg=colour_books_search, fg=colour_books, font=("Arial", 16, "bold"))
            found_book_label_rating = tk.Label(window_search, text=f"{found_book.rating} / 10",
                                               bg=colour_books_search, fg=colour_books, font=("Arial", 16, "bold"))
            found_book_label_title.grid(row=3 + idx, column=0, columnspan=1, pady=20, padx=10, sticky="nsew")
            found_book_label_author.grid(row=3 + idx, column=1, columnspan=1, pady=20, padx=10, sticky="nsew")
            found_book_label_year.grid(row=3 + idx, column=2, columnspan=1, pady=20, padx=10, sticky="nsew")
            found_book_label_rating.grid(row=3 + idx, column=3, columnspan=1, pady=20, padx=10, sticky="nsew")

    def search_books(*args):
        search_term = search_var.get().strip().lower()
        if not search_term:
            display_search_results([])
            return

        found_books = [
            book for book in all_books
            if (search_term in book.title.lower() or
                search_term in book.author.lower() or
                search_term in book.year.lower())
        ]
        display_search_results(found_books)

    window_search = tk.Toplevel()
    window_search.title("Search Books")
    window_search.geometry("800x500")
    window_search.minsize(500, 500)
    window_search.configure(bg=colour2)

    window_search.grid_columnconfigure(0, weight=1)
    window_search.grid_columnconfigure(1, weight=0)
    window_search.grid_rowconfigure(2, weight=0)
    window_search.grid_rowconfigure(1, weight=0)

    settings_search()

    # Search field with StringVar
    search_var = tk.StringVar()
    search_var.trace("w", search_books)  # Call search_books on any change
    entry_search_field = tk.Entry(window_search, textvariable=search_var, bg=colour9, fg=colour9_text,
                                  font=("Arial", 16))
    entry_search_field.grid(row=1, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")

    # Initial empty search results
    display_search_results([])

    window_search.mainloop()


def display_books(window_v, start_category_to_read_v):
    to_read_books = []
    read_books = []
    for book in all_books:
        if book.status == "to_read":
            to_read_books.append(tk.Label(window_v, text=book.title, bg=colour5, fg=colour5_text,
                                          font=("Arial", 15, "bold")))
        elif book.status == "read":
            read_books.append(tk.Label(window_v, text=book.title, bg=colour8, fg=colour8_text,
                                       font=("Arial", 15, "bold")))

    to_read_books_counter = 0
    read_books_counter = 0
    for book in to_read_books:
        book.grid(row=4 + to_read_books_counter, column=start_category_to_read_v, padx=5, pady=5, sticky="nsew")
        to_read_books_counter += 1
    for book in read_books:
        book.grid(row=4 + read_books_counter, column=0, padx=5, pady=5, sticky="nsew")
        read_books_counter += 1


def display_ratings(window_v, column_for_rating_v):
    ratings_read = []
    ratings_to_read = []
    for book in all_books:
        if book.status == "read":
            ratings_read.append(tk.Label(window_v, text=f" {book.rating} / 10 ", bg=colour8, fg=colour8_text,
                                font=("Arial", 15, "bold")))
        elif book.status == "to_read":
            ratings_to_read.append(tk.Label(window_v, text=f" {book.rating} / 10 ", bg=colour5, fg=colour8_text,
                                   font=("Arial", 15, "bold")))

    ratings_counter = 0
    for rating in ratings_read:
        rating.grid(row=4 + ratings_counter, column=column_for_rating_v, padx=5, pady=5, sticky="nsew")
        ratings_counter += 1

    ratings_counter = 0
    for rating in ratings_to_read:
        rating.grid(row=4 + ratings_counter, column=start_category_to_read + column_for_rating_v,
                    padx=5, pady=5, sticky="nsew")
        ratings_counter += 1


def display_authors(window_v, column_for_author_v):
    authors_read = []
    authors_to_read = []
    for book in all_books:
        if book.status == "read":
            authors_read.append(tk.Label(window_v, text=f" {book.author}", bg=colour8, fg=colour8_text,
                                font=("Arial", 15, "bold")))
        if book.status == "to_read":
            authors_to_read.append(tk.Label(window_v, text=f" {book.author}", bg=colour5, fg=colour5_text,
                                   font=("Arial", 15, "bold")))

    authors_counter = 0
    for author in authors_read:
        author.grid(row=4 + authors_counter, column=column_for_author_v, padx=5, pady=5, sticky="nsew")
        authors_counter += 1

    authors_counter = 0
    for author in authors_to_read:
        author.grid(row=4 + authors_counter, column=start_category_to_read + column_for_author_v,
                    padx=5, pady=5, sticky="nsew")
        authors_counter += 1


def display_years(window_v, column_for_year_v):
    years_read = []
    years_to_read = []
    for book in all_books:
        if book.status == "read":
            years_read.append(tk.Label(window_v, text=f" {book.year}", bg=colour8, fg=colour8_text,
                                       font=("Arial", 15, "bold")))
        if book.status == "to_read":
            years_to_read.append(tk.Label(window_v, text=f" {book.year}", bg=colour5, fg=colour5_text,
                                          font=("Arial", 15, "bold")))

    years_counter = 0
    for author in years_read:
        author.grid(row=4 + years_counter, column=column_for_year_v, padx=5, pady=5, sticky="nsew")
        years_counter += 1

    years_counter = 0
    for author in years_to_read:
        author.grid(row=4 + years_counter, column=start_category_to_read + column_for_year_v,
                    padx=5, pady=5, sticky="nsew")
        years_counter += 1


def display_new_book_button(window, start_category_to_read_v):
    new_book_button = tk.Button(window, text="Add new book", width=20, height=2, bg=colour9, fg=colour9_text,
                                font=("Arial", 20, "bold"), command=lambda: window_add_book(window))
    new_book_button.grid(row=22, column=0, columnspan=start_category_to_read_v, pady=20, padx=80, sticky="sw")
    new_book_button.configure(bg=colour9, fg=colour9_text, activebackground=colour1, activeforeground=colour1_text)


def display_settings_button(window_v, start_category_to_read_v):
    settings_button = tk.Button(window_v, text="Settings", width=20, height=2, bg=colour9, fg=colour9_text,
                                font=("Arial", 20, "bold"),
                                command=lambda: window_settings(window_v))
    settings_button.grid(row=22, column=start_category_to_read_v, columnspan=start_category_to_read_v, pady=20, padx=80,
                         sticky="sw")
    settings_button.configure(bg=colour9, fg=colour9_text, activebackground=colour1, activeforeground=colour1_text)


def display_status_change_button(window_v, start_category_to_read_v):
    change_status_button = tk.Button(window_v, text="Change status", width=20, height=2, bg=colour9, fg=colour9_text,
                                     font=("Arial", 20, "bold"),
                                     command=lambda: window_status_change(window_v))
    change_status_button.grid(row=22, column=0, columnspan=start_category_to_read_v, pady=20, padx=80,
                              sticky="se")
    change_status_button.configure(bg=colour9, fg=colour9_text, activebackground=colour1, activeforeground=colour1_text)


def display_search_books_button(window_v, start_category_to_read_v):
    settings_button = tk.Button(window_v, text="Search", width=20, height=2, bg=colour9, fg=colour9_text,
                                font=("Arial", 20, "bold"),
                                command=lambda: window_search_books())
    settings_button.grid(row=22, column=start_category_to_read_v, columnspan=start_category_to_read_v, pady=20, padx=80,
                         sticky="se")
    settings_button.configure(bg=colour9, fg=colour9_text, activebackground=colour1, activeforeground=colour1_text)


def display_categories(window):
    category_read = tk.Label(window, text="read", height=1, bg=colour6, fg=colour6_text, font=("Arial", 20, "bold"))
    category_to_read = tk.Label(window, text="to read", height=1, bg=colour3, fg=colour3_text,
                                font=("Arial", 20, "bold"))

    category_title = tk.Label(window, text="Title", bg=colour7, fg=colour7_text, font=("Arial", 20, "bold"))
    category_author = tk.Label(window, text="Author", bg=colour7, fg=colour7_text, font=("Arial", 20, "bold"))
    category_year = tk.Label(window, text="Year", bg=colour7, fg=colour7_text, font=("Arial", 20, "bold"))
    category_rating = tk.Label(window, text="Rating", bg=colour7, fg=colour7_text, font=("Arial", 20, "bold"))

    category_title2 = tk.Label(window, text="Title", bg=colour4, fg=colour4_text, font=("Arial", 20, "bold"))
    category_author2 = tk.Label(window, text="Author", bg=colour4, fg=colour4_text, font=("Arial", 20, "bold"))
    category_year2 = tk.Label(window, text="Year", bg=colour4, fg=colour4_text, font=("Arial", 20, "bold"))
    category_rating2 = tk.Label(window, text="Rating", bg=colour4, fg=colour4_text, font=("Arial", 20, "bold"))

    category_read.grid(row=1, column=0, columnspan=start_category_to_read, pady=20, sticky="nsew")
    category_to_read.grid(row=1, column=start_category_to_read, columnspan=start_category_to_read,
                          pady=20, sticky="nsew")

    category_title.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    category_title2.grid(row=2, column=start_category_to_read, padx=5, pady=5, sticky="nsew")

    start_next_category = 1  # so the next category starts at the right column

    if show_author:
        category_author.grid(row=2, column=start_next_category, padx=5, pady=5, sticky="nsew")
        category_author2.grid(row=2, column=start_category_to_read + start_next_category, padx=5, pady=5, sticky="nsew")
        start_next_category += 1
    if show_year:
        category_year.grid(row=2, column=start_next_category, padx=5, pady=5, sticky="nsew")
        category_year2.grid(row=2, column=start_category_to_read + start_next_category, padx=5, pady=5, sticky="nsew")
        start_next_category += 1
    if show_rating:
        category_rating.grid(row=2, column=start_next_category, padx=5, pady=5, sticky="nsew")
        category_rating2.grid(row=2, column=start_category_to_read + start_next_category, padx=5, pady=5, sticky="nsew")


def display_categories_content(window_v, column_for_author_v, column_for_year_v, column_for_rating_v):
    if show_author:
        display_authors(window_v, column_for_author_v)
    if show_year:
        display_years(window_v, column_for_year_v)
    if show_rating:
        display_ratings(window_v, column_for_rating_v)


def set_categories(show_author_v, show_year_v, show_rating_v):
    column_for_year_v = 0
    column_for_author_v = 0
    column_for_rating_v = 0

    start_category_to_read_v = 1  # Start with 1 for the title column
    if show_author_v:
        column_for_author_v = start_category_to_read_v
        start_category_to_read_v += 1
    if show_year_v:
        column_for_year_v = start_category_to_read_v
        start_category_to_read_v += 1
    if show_rating_v:
        column_for_rating_v = start_category_to_read_v
        start_category_to_read_v += 1

    return (start_category_to_read_v, show_author_v, show_year_v, show_rating_v,
            column_for_author_v, column_for_year_v, column_for_rating_v)


def window_settings(window):
    window_categories = tk.Tk()
    window_categories.title("Set Categories")
    window_categories.geometry("500x500")
    window_categories.minsize(500, 700)
    window_categories.configure(bg=colour2)

    headline_categories = tk.Label(window_categories, text="Set Categories", height=1, bg=colour1, fg=colour1_text,
                                   font=("Arial", 25, "bold"))
    headline_categories.grid(row=0, column=0, columnspan=20, pady=20, sticky="nsew")

    def toggle_switch(switch_var):
        if switch_var.get():
            switch_var.set(False)
        else:
            switch_var.set(True)

    switch_state_author = tk.BooleanVar(value=False)
    switch_state_year = tk.BooleanVar(value=False)
    switch_state_rating = tk.BooleanVar(value=False)
    show_author_switch = tk.Checkbutton(window_categories, text="Author", onvalue=True, offvalue=False, width=15,
                                        indicatoron=False, height=2, font=("Arial", 20, "bold"),
                                        variable=switch_state_author,
                                        command=lambda: toggle_switch(switch_state_author))
    show_year_switch = tk.Checkbutton(window_categories, text="Year", onvalue=True, offvalue=False, width=15,
                                      indicatoron=False, height=2, font=("Arial", 20, "bold"),
                                      variable=switch_state_year,
                                      command=lambda: toggle_switch(switch_state_year))
    show_rating_switch = tk.Checkbutton(window_categories, text="Rating", onvalue=True, offvalue=False, width=15,
                                        indicatoron=False, height=2, font=("Arial", 20, "bold"),
                                        variable=switch_state_rating,
                                        command=lambda: toggle_switch(switch_state_rating))

    show_author_switch.grid(row=1, column=1, pady=10, padx=15, sticky="nsew")
    show_year_switch.grid(row=2, column=1, pady=10, padx=15, sticky="nsew")
    show_rating_switch.grid(row=3, column=1, pady=10, padx=15, sticky="nsew")

    show_year_switch.configure(bg=colour3, fg=colour3_text, activebackground=colour7, activeforeground=colour7_text,
                               selectcolor=colour6)
    show_author_switch.configure(bg=colour3, fg=colour3_text, activebackground=colour7, activeforeground=colour7_text,
                                 selectcolor=colour6)
    show_rating_switch.configure(bg=colour3, fg=colour3_text, activebackground=colour7, activeforeground=colour7_text,
                                 selectcolor=colour6)

    def sort_books(category_sort_v):
        global category_sort
        category_sort_string = ["Title", "Author", "Year", "Rating", "Entry Time"]
        if category_sort_v == 4:  # Reset to 0 after sorting by entry time
            category_sort_v = -1
        category_sort_v += 1
#        print(f"Current sorting category: {category_sort_v}")
        if category_sort_v == 0:
            all_books.sort(key=lambda book: book.title.lower())
            print("Sorting books by title")
        elif category_sort_v == 1:
            all_books.sort(key=lambda book: book.author.lower())
            print("Sorting books by author")
        elif category_sort_v == 2:
            all_books.sort(key=lambda book: int(book.year))
            print("Sorting books by year")
        elif category_sort_v == 3:
            all_books.sort(key=lambda book: int(book.rating) if book.rating.isdigit() else 0)
            print("Sorting books by rating")
        elif category_sort_v == 4:
            all_books.sort(key=lambda book: datetime.strptime(book.entry_time, "%Y-%m-%d %H:%M:%S"))
            print("Sorting books by entry time")
#        print(f"Sorting books by category ({category_sort_string[category_sort_v]})")
        print(category_sort_v)

        save_data(all_books)
        category_sort = category_sort_v
        sort_button.config(text="Sort Books by " + category_sort_string[category_sort_v])
        return category_sort_v

    sort_button = tk.Button(window_categories, text="click to sort books", width=25, height=2, bg=colour9,
                            fg=colour9_text, font=("Arial", 20, "bold"), command=lambda: sort_books(category_sort))
    sort_button.grid(row=5, column=1, pady=10, padx=15, sticky="nsew")
    sort_button.configure(bg=colour9, fg=colour9_text, activebackground=colour1, activeforeground=colour1_text)

    def save_categories(author_state, year_state, rating_state):
        global show_author, show_year, show_rating
        show_author = author_state.get()
        show_year = year_state.get()
        show_rating = rating_state.get()
        print(f"Author: {show_author}, Year: {show_year}, Rating: {show_rating}")
        (start_category_to_read_v, show_author_v, show_year_v, show_rating_v, column_for_author_v, column_for_year_v,
         column_for_rating_v) = refresh_books(window)
        display_everything(window, column_for_author_v, column_for_year_v, column_for_rating_v)
        window_categories.destroy()

    save_button = tk.Button(window_categories, text="Save", width=10, height=2, bg="white", fg="black",
                            font=("Arial", 20, "bold"),
                            command=lambda: save_categories(switch_state_author, switch_state_year,
                                                            switch_state_rating))
    save_button.grid(row=7, column=1, pady=20, padx=15, sticky="s")
    save_button.configure(bg=colour9, fg=colour9_text, activebackground=colour1, activeforeground=colour1_text)

    window_categories.grid_columnconfigure(0, weight=1)
    window_categories.grid_columnconfigure(0, weight=1)
    window_categories.grid_columnconfigure(2, weight=1)
    window_categories.grid_rowconfigure(4, weight=1)
    window_categories.grid_rowconfigure(6, weight=2)


def display_everything(window_v, column_for_author_v, column_for_year_v, column_for_rating_v):
    display_categories(window_v)
    display_books(window_v, start_category_to_read)
    display_categories_content(window_v, column_for_author_v, column_for_year_v, column_for_rating_v)
    display_new_book_button(window_v, start_category_to_read)
    display_settings_button(window_v, start_category_to_read)
    display_status_change_button(window_v, start_category_to_read)
    display_search_books_button(window_v, start_category_to_read)


def visualize():
    # tkinter window
    window = tk.Tk()
    window.title("Book Manager")
    window.geometry("2000x1300")
    window.configure(bg=colour2)
    window.minsize(700, 700)
    # window.maxsize(1000, 1000)
    headline = tk.Label(window, text="book list", height=1, bg=colour1, fg=colour1_text, font=("Arial", 50, "bold"))

    headline.grid(row=0, column=0, columnspan=20, pady=20, sticky="nsew")

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(start_category_to_read, weight=1)
    window.grid_rowconfigure(20, weight=1)  # Row for books expands
    window.grid_rowconfigure(21, weight=0)  # Row for button stays fixed

    # call functions
    display_everything(window, column_for_author, column_for_year, column_for_rating)

    window.mainloop()




show_author = True
show_year = True
show_rating = True
category_sort = -1


start_category_to_read, show_author, show_year, show_rating, column_for_author, column_for_year, column_for_rating = (
    set_categories(show_author, show_year, show_rating))
# print(column_for_author, column_for_year, column_for_rating)

(colour1, colour2, colour3, colour4, colour5, colour6, colour7, colour8, colour9,
 colour1_text, colour2_text, colour3_text, colour4_text, colour5_text, colour6_text, colour7_text,
 colour8_text, colour9_text) = set_colours()

all_books = load_data()
# for book_v in all_books:
#    print(f"Loaded book: {book_v.title} by {book_v.author}, Year: {book_v.year}, Rating: {book_v.rating}, "
#          f"Status: {book_v.status}, Entry Time: {book_v.entry_time}")

visualize()
