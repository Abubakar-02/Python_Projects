
class Book:
    def __init__(self,name, writer, pages):
        self.name=name
        self.writer=writer
        self.pages=pages

    def info(self):
        
            print(f"Name : {self.name} | , Writer :{self.writer} |, Pages : {self.pages}")


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.name} add ho gayi hey")

    def show_books(self):
        if len(self.books) == 0:
            print("Library khali hey")
        else:
            for book in self.books:
                book.info()

    def remove_book(self, name):
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
                print(f"{name} remove ho gai")
                return
        print(f"{name} library mein nahi mili")
    def search_book(self,name):
        for book in self.books:
            if book.name==name:
                book.info()
                return       
        print(f"{name} library mein nahi mili")

library = Library()

library.add_book(Book("Physics"," Punjab text book board" , 250))
library.add_book(Book("Chemistry", "Punjab text book board ", 280))
library.add_book(Book("Biology","Punjab text book board ", 222))
library.add_book(Book("Mathematics", "Punjab text book board" , 283))
library.add_book(Book("English", "Punjab text book board" , 245))
library.add_book(Book("Pak Studies", "Punjab text book board" , 213))
library.add_book(Book("Urdu", "Punjab text book board" , 254))
library.add_book(Book("Islamiyat", "Punjab text book board" , 290))


while True:
    print("n\ Library Management System ")
    print("1. Book add kro")
    print("2. Book remove kro")
    print("3. Book search kro")
    print("4. Sab books dekho")
    print("5. Exit")

    choice = input("Apna Choice likho (1-5):")
    
    if choice == "1":
        name = input("Name of book")
        writer= input("Name of write")
        pages= int(input("pages: "))
        new_book = Book(name,writer,pages)
        library.add_book(new_book)

    elif choice == "2":
        name= input("Konsi book remove krni hey")
        library.remove_book(name)

    elif choice == "3":
        name= input(" Konsi book search krni hey :")
        library.search_book(name)

    elif choice == "4":
        library.show_books()

    elif choice == "5":
        print("Library Management system bnd ho chuka hey")
        break
    else:
        print(" Ghalat choice : 1-5 may sey chose kro")