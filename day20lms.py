# LMS System using OOP
# Library Management System

# Ask the user to create or visit the LMS
# if create: ask name and address of LMS and store it in a list
# if visit: ask the name of LMS to visit and check if LMS is present or not
    # if lms found, print lms visited
        # Show the LMS menu: add book, remove book, search book, view books
        # add book: ask book details with type and store them in the list of that LMS 
        # remove, search: Ask which book to remove/search, and find that book and display the book or remove it
        # view: DIsplay all the books availabe
    # else: print lms not found 
    
def operation(method, lms_object):
    found = False
    book_name = input("Enter book name: ")
    for book in lms_object.books:
        if book_name == book.title:
            print(f"{book_name} Found")
            found = True
            index = lms_object.books.index(book)
            if method == 'search':
                print(f"Book found at index {index}")
            else:
                lms_object.books.remove(book)
                print(f"{book_name} removed successfully")
    if not found:
        print("Book not found")

    
lms_list = []
class LMS:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
class Ebook(Book):
    def __init__(self, title, author, pages, size):
        super().__init__(title, author, pages)
        self.size = size 

while True:
    choice = input("Enter 1 to create, 2 to visit the LMS, 3 to exit: ")
    match choice:
        case '1':
            name = input("ENter the name of LMS: ")
            address = input("ENter the address of LMS: ")
            lms = LMS(name, address)
            lms_list.append(lms)
        case '2':
            is_visited = False
            name = input("Enter the name of LMS: ")
            address = input("ENter the address of LMS: ")
            for i in lms_list:
                if name == i.name and address == i.address:
                    print("Lms Found. You are welcome to LMS")
                    is_visited = True
                    while True:
                        choice = input("Enter 1 to add book, 2 to search book, 3 to remove book, 4 to view books, 5 to exit: ")
                        match choice:
                            case '1':
                                title = input("Enter book title: ")
                                author = input("ENter book author: ")
                                pages = input("Enter book pages: ")
                                type = input("Physical or Online?(p/o): ")
                                if type == 'p':
                                    book = Book(title, author, pages)
                                    i.books.append(book)
                                elif type == 'o':
                                    size = input("Enter book size: ")
                                    ebook = Ebook(title, author, pages, size)
                                    i.books.append(ebook)
                            case '2':
                                operation('search', i)
                            case '3':
                                operation('remove', i)
                            case '4':
                                for book in i.books:
                                    print(f"Title : {book.title}")
                                    print(f"Author : {book.author}")
                                    print(f"Pages : {book.pages}")
                                    
                                    if "Ebook" in str(book):
                                        print(f"Size : {book.size}")
                                    print()
                            case '5':
                                print("Thank you for using our Library")
                                break
                            case _:
                                print("Invalid Input")
            if not is_visited:
                print("LMS not found. Please try a new LMS.")
        case '3':
            print("Thank you")
            break
        case _:
            print("Invalid Input")