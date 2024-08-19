class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)
    
    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return book
        else:
            return 'Book not available'

if __name__ == "__main__":
    library = Library()
    library.add_book('1984')
    library.add_book('Brave New World')
    print(f"Borrowing 1984: {library.borrow_book('1984')}")
    print(f"Borrowing The Catcher in the Rye: {library.borrow_book('The Catcher in the Rye')}")