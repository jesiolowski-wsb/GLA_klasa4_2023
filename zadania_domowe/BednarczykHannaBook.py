class Book:
    available = "Available" # default
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def attributes(self):
        print(f"{self.title}\t{self.author}\t{self.year}\t{self.available}")

class Library:
    def __init__(self):
        self.books = []
        self.borrowed = []
    def add_book(self,book):
        self.books.append(book)
    def display(self):
        titles = []
        for book in self.books:
            titles.append(book.title)
        print(titles)
    def borrow_book(self,title):
        if bool(self.books) == 0:
            print("sorry, the library is empty")
        else:
            found = False
            for book in self.books:
                if book.title == title:
                    if book.available == "Available":
                        self.borrowed.append(book)
                        self.books.remove(book)
                        book.available = "Not Available"
                        found = True
                        print(f"you borrowed {title}")
                        break
            if found == False:
                print("sorry, this book isn't in the library")
    def return_book(self,title):
        borrowed = False
        in_lib = False
        for book in self.books:
            if book.title == title:
                print("this book is in library")
                in_lib = True
                break
        if in_lib == False:
            for book in self.borrowed:
                if book.title == title:
                    self.books.append(book)
                    self.borrowed.remove(book)
                    print(f"you returned {title}")
                    borrowed = True
                    break
        if borrowed == False and in_lib == False:
            print("this book wasn't borrowed from the library.")
        

library = Library()

tjjsacahtrw =  Book("The Jewish/Japanese Sex and Cookbook and How to Raise Wolves", "Jack Douglas", 1974)
htttycags = Book("How to Talk to Your Cat About Gun Safety", "Zachary Auburn", 2016)
hp = Book("Harry Potter", "Just Kidding Rowling", 1997)
th = Book("Thunderhead", "I don't remember & I'm too lazy to look up", 2018)
ladtaody = Book("Light and Dark the Adventures of Dark Yagami", "a child with internet access and an IQ somewhere in the negatives", 2012)

library.borrow_book("Thunderhead")
library.add_book(htttycags)
library.add_book(hp)
library.add_book(ladtaody)
library.add_book(th)
library.display()

library.borrow_book("Light and Dark the Adventures of Dark Yagami")
library.display()
library.borrow_book("Light and Dark the Adventures of Dark Yagami")
library.return_book("Light and Dark the Adventures of Dark Yagami")
library.return_book("How to Talk to Your Cat About Gun Safety")
library.return_book("fghhj")
