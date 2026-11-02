#library management system day 20 update with try except, no adding 2 same book of same type
import json

class LMS:
  def __init__(self, name, address):
    self.name=name
    self.address=address
    self.books=[]

class Books:
  def __init__(self, title, author, page):
    self.title=title
    self.author=author
    self.page=page

class Ebook(Books): 
  def __init__(self,title, author, page, size):
    super().__init__(title, author, page)
    self.size=size
 

def save_file(lms_list):
    data=""
    for l in lms_list:
        dict_lib={"Name of library": l.name, "Address of the library": l.address, "Books": []}
        for b in l.books:
            if "Ebook" not in str(b):
                book_data={"Book title" : b.title, "Author": b.author, "Number of pages": b.page, "Book type" : "Physical"}
            else:
                book_data={"Book title" : b.title, "Author": b.author, "Number of pages": b.page, "Book size in mb": b.size, "Book type" : "Ebook"}
            dict_lib["Books"].append(book_data)
        data+=json.dumps(dict_lib)+"*"
    file=open("library.txt", "w")
    file.write(data)
    file.close()
    print("LMS added to the file.")

def load_file():
    try:
        file=open("library.txt", "r")
        content=file.read()
        file.close()
        list_lib=content.split("*")
    except:
        return []
    lms_list=[]
    for lms_data in list_lib:
        if lms_data!="":
            dict_lms=json.loads(lms_data)
            lms=LMS(dict_lms["Name of library"], dict_lms["Address of the library"])
            for book_data in dict_lms["Books"]:
                if book_data["Book type"]=="Ebook":
                    book=Ebook(book_data["Book title"], book_data["Author"], book_data["Number of pages"], book_data["Book size in mb"])
                else:
                    book=Books(book_data["Book title"], book_data["Author"], book_data["Number of pages"])
                lms.books.append(book)
            lms_list.append(lms)
    return lms_list


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


lms_list=load_file()

while True:
    choice=input("Enter 1 to create, 2 to visit and 3 to exit: ")
    match choice:
        case '1':
            name=input("Enter the name of LMS: ")
            address=input("Enter address of LMS: ") 
            lms=LMS(name, address)
            lms_list.append(lms)
            save_file(lms_list)
        case '2':
            is_visited=False
            name=input("Enter the name of LMS: ")
            address=input("Enter address of LMS: ")
            for i in lms_list:
                if name==i.name and address==i.address:
                    print("LMS found. Welcome to LMS")
                    is_visited=True
                    while True:
                      choice=input("Enter 1 to add book, 2 to search book, 3 to remove book, 4 to view book and 5 to exit: ")
                      match choice:
                          case '1':
                                try:
                                    name=input("Enter the title of book: ")
                                    author=input("Enter the author of book: ")
                                    page=int(input("Enter the no of pages of book: "))
                                    type=input("Physical or online(p/o)? ")
                                    if type!="p" and type!="o":
                                        print("Only 'p' and 'o' is accepted as input")
                                    else:
                                        is_present=False
                                        for j in i.books:
                                            if type =='p':
                                                if name==j.title and "Ebook" not in str(j):
                                                    print("The physical book already exists.")
                                                    is_present=True
                                                    break
                                            elif type=='o':
                                                if name==j.title and "Ebook" in str(j):
                                                    print("The Ebook already exists")  
                                                    is_present=True
                                                    break
                                        if not is_present:
                                            if type=="p":              
                                                book=Books(name, author, page)
                                                i.books.append(book)
                                                save_file(lms_list)
                                            else:
                                                try:
                                                    size = float(input("Enter book size in MB: "))
                                                    if size<=0:
                                                        print("Invalid book size: size must be greater than zero.")
                                                    else:
                                                        book=Ebook(name, author, page, size)
                                                        i.books.append(book)  
                                                        save_file(lms_list)
                                                except Exception as e:
                                                    print("An error occured: ",e)
                                except Exception as e:
                                    print("An error occured: ", e)     
                          case '2':
                              operation('search', i)
                          case '3':
                              operation('remove', i)
                          case '4':
                              for book in i.books:
                                  print("Book title: ", book.title)
                                  print("Book author: ", book.author)
                                  print("Number of pages: ", book.page)
  
                                  if "Ebook" in str(book):
                                      print("Book size: ", book.size)
                                  print()
                          case '5':
                              print ("Thank you for visiting our Library")
                              break
                          case _:
                              print("Invalid input")
            if not is_visited:
                print("LMS not found")
            
        case '3':
            print("Thank you")
            break
        case _:
            print("Invalid input")