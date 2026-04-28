from utilities import books
def add_book():
    bno=input("Enter new book number:")
    bname=input("Enter new book name:")
    
    if bno in books:
        print("Book number already exits!")
    else:
        books[bno]=bname
        print("Book added successfully")
