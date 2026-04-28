from utilities import books, issued_books
from datetime import date, timedelta

def issue_book():
    s_name=input("Enter your name:")
    s_id=input("Enter your id:")
    
    bno=input("Please Enter A Book number to issue:")
    
    if bno in books:
        doi= date.today()
        issued_books[bno]={
            "book name":books[bno],
            "student":s_name,
            "id":s_id,
            "date":str(doi)}
        print("\nBook successfully issued ")
        print("Details:",issued_books[bno])
        print("Return within 7 days to avoid fine.")
        print("Fine will be imposed as follows:")
        print("Week 1:10rs/day\nWeek 2:20rs/day\nWeek 3:30rs/day")
        b=books.pop(bno)
        
    else:
        print("***Invalid book number or Book is already issued***")


