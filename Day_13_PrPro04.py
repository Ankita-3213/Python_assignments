#Library Management System

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You borrowed '{self.title}'. Copies left: {self.copies}")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        self.copies += 1
        print(f"You returned '{self.title}'. Copies available: {self.copies}")

book = Book("The Monk Who Sold His Ferrari", "Robin Sharma", 2)

book.borrow_book()
book.borrow_book()
print(book.copies)
book.return_book()


