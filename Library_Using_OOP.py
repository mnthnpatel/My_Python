class Library:

    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("The Present Books In Libary Are :- ")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You Have Been Issued {bookName}. Please Keep It Safe And Return It Within 30 Days.")
            self.books.remove(bookName)
            return True
        else: 
            print("Sorry! This Book Is Either Not Available Or Has Been Already Issued To Someone Else. Please Wait Until The Book Is Available. ")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thank You For Returning This Book! Hope You Enjoyed Reading It.")



class Student:
    
    def requestBook(self):
        self.book = input("Enter The Name Of The Book You Want To Borrow :- ")
        return self.book
        
    def rerurnBook(self):
        self.book = input("Enter The Name Of The Book You Want To Return Or Add :-  ")
        return self.book

student = Student()

if __name__ == "__main__":
    centralLibrary = Library(["Python Notes", "Django", "Algorithms","Data Structure", "Machine Learning", "Flask"])
    # centralLibrary.displayAvailableBooks()


    while(True):
        welcomeMsg = '''\n ===== Welcome To  Central Library ===== 
        Please Choose An Option
        1. List All The Books
        2.Request A Book
        3.Add/Return A Book
        4.Exit The Library
        '''
        print(welcomeMsg)

        a = int(input("Enter A Choice :- "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.rerurnBook())
        elif a == 4:
            print("Thanks For Choosing Central Library!")
            exit()
        else:
            print("Invalid Choice!")