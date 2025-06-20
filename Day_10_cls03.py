class Library:
    def __init__(self):
        self.books = []  # List of dictionaries: [{"title": str, "author": str, "available": bool}]

    def add_book(self, title, author):
        """Add a new book to the library."""
        self.books.append({"title": title, "author": author, "available": True})
        print(f"Book '{title}' added.")

    def borrow_book(self, title):
        """Borrow a book if available."""
        for book in self.books:
            if book["title"] == title:
                if book["available"]:
                    book["available"] = False
                    print(f"You borrowed '{title}'")
                    return
                else:
                    print(f"'{title}' is currently unavailable.")
                    return
        print(f"Book '{title}' not found.")

    def get_available_books(self):
        """List all available books."""
        return [book for book in self.books if book["available"]]

library = Library()
library.add_book("Python Programming", "Siddhi")
library.add_book("Data Structures", "Arya")
library.add_book("OOPS in Java", "Vidya")

library.borrow_book("Python Programming") 
library.borrow_book("Python Programming")
print(library.get_available_books())  


