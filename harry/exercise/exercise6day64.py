# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and 
# show how you can print all books, add a book and get the number of books using different methods. 
# Show that your program doesnt persist the books after the program is stopped

# no-->noumber of books
# books --> list of book 
# book indiviadual books that u want to add

class Library:
    def __init__(self):
        self.noBooks=0 # class variable 
        self.books=[]  # class varible hai but particular liabray ke liye change ho jayega 
    def addBook(self,book):
        self.books.append(book) # adding number of books in list of books 
        self.noBooks=len(self.books) # associating noBooks class variable 
    def showInfo(self):
        print(f"the library has {self.noBooks} books, the books are ")  
        for  book in self.books:
            print(book)

l1=Library()
l1.addBook("harry Potter1")
l1.addBook("harry pottery2")
l1.addBook("harry book 2")
l1.showInfo()






