


class Book:
    def __init__(self,title,author,is_checked_out=False):
        self.title=title
        self.author = author
        self._is_checked_out = is_checked_out



class Library:
    def __init__(self):
         self._books = []


    def add_book(self,book):
        self.books.append(book)

"check_out", "return_book(self)", "True"

book1 = Library.add_book(Book("Brave New World", "Aldous Huxley"))


print(book1.books)