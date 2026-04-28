from utilities import books, issued_books, returned_books
from datetime import datetime, date

def isfine(days_used):
    if days_used<=7:
        return 0
    else:
        extra = days_used - 7
        fine=0
        for i in range(extra):
            fine+= 10*i
        return fine
    
def return_book():
    bno=input("Enter book number to return:")
    if bno in issued_books:
        record= issued_books[bno]
        doi= datetime.strptime(record["date"],"%Y-%m-%d")
        doi= doi.date()

        today=date.today()
        days_used = (today - doi).days

        fine = isfine(days_used)

        books[bno]=record["book name"]

        returned_books[bno]=record
        print(returned_books[bno])

        del issued_books[bno]

        print("Book returned successfully")
        print("Days used:",days_used)
        print("Fine:",fine)
    else:
        print("***Book was not issued***")
