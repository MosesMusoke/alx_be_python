# Base class - Book
class Book:
    def __init__(self, title, author):
        """Initializes the common attributes of a book: title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of the Book instance."""
        return f"Book: {self.title} by {self.author}"

# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initializes the attributes of an EBook, including file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation of the EBook instance."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initializes the attributes of a PrintBook, including page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of the PrintBook instance."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition - Library
class Library:
    def __init__(self):
        """Initializes a Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of each book in the library."""
        for book in self.books:
            print(book)
