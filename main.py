from add_book import add_book
from show_book import show_book
from issue_book import issue_book
from return_book import return_book

def library():
    while True:
        print("---Library Menu---")
        print("1.Add Books")
        print("2.Show Books")
        print("3.Issue Books")
        print("4.Return Books")
        print("5.Exit")

        choice=input("Enter Your Choice:")
        if not choice.isdigit():
            print("*** Please enter number of your choice ***")
            continue
        choice=int(choice)
        if choice==1:
            add_book()
        elif choice==2:
             show_book()
        elif choice==3:
            issue_book()
        elif choice==4:
            return_book()
        elif choice==5:
            print("Exiting Library")
            return False
        else:
            print("*** Please enter a valid choice ***")
library()


        
