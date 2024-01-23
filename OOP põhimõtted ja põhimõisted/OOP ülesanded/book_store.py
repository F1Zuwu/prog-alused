"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if a book can be added to the store.

        It is possible to add a book to the book store if:
        1. The book with the same author and title is not yet present in this book store.
        2. The book's rating is greater than or equal to the store's rating.
        """
        for existing_book in self.books:
            if existing_book.title == book.title and existing_book.author == book.author:
                return False
        return book.rating >= self.rating

    def add_book(self, book: Book):
        """
        Add a new book to the book store if possible.

        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if a book can be removed from the store.

        A book can be successfully removed if it is present in the store.

        """
        return book in self.books

    def remove_book(self, book: Book):
        """
        Remove a book from the store if possible.

        """
        if self.can_remove_book(book):
            self.books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in the current store.

        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        """
        return sorted(self.books, key=lambda x: x.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of books with the highest rating.

        """
        max_rating = max(book.rating for book in self.books)
        return [book for book in self.books if book.rating == max_rating]
