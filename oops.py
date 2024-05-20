class Book:
    def __init__(self,title,author,isbn) :
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Patron:

    def __init__(self,name,patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self,book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed {self.book}")


class library:

    def __init__(self) :

        
        
        