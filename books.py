class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year
    self. is_available = True

class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def display_books(self):
    available_books = [book.title for book in self.books if book.is_available]
    if available_books:
      print("available books: ", " ,".join(available_books))
    else:
      print("no available books")

def borrow_book(self, title):
  for book in self.books:
    if book.title == title and book.is_available:
      book.is_available = False
      print(f"You have borrowed {title}.")
      return
    print(f"{title} is not available")

def return_book(self, title):
  for book in self.books:
    if book.title == title and book.is_available:
      book.is_available = True
      print(f"You have returned {title}.")
      return
    print(f"{title} is not available")

b1 = Book("Lalka", "Bolesław Prus", 1889)
b2 = Book("Zbrodnia i Kara", "Fiodor Dostojewski", 1866)
b3 = Book("Wesele", "Stanisław Wyspiański", 1901)

library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.display_books()
library.borrow_book("Zbrodnia i Kara")
library.display_books()

library.return_book("Zbrodnia i Kara")
library.display_books()
      
    


    
  
