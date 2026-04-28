from utilities import books

def show_book():
    print("Available books:")
    for bno, bname in books.items():
        print(f"{bno} | {bname}")

