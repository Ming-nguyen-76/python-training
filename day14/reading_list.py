FILE_NAME = "day14/book.csv"
DAY14 = "book.csv"

menu = """Enter
'a' - add a book
'r' - retrive books list
's' - search book
'm' - mark book
'd' - delete book
'q' - quit
your choice: """


def add_book():
    book_name = input("Enter book name: ").title().strip()
    book_author = input("Enter book author: ").title().strip()
    year_release = int(input("Enter year released: "))
    read = input("Have you read the book?: ")
    with open(DAY14, "a") as sach:
        sach.write(f"{book_name},{book_author},{year_release},{read}\n")


def retrive_books():
    with open(DAY14) as book:
        doc = book.readlines()
    if len(doc) == 0:
        print("There is no book in book list")
    else:
        for row in doc:
            name, author, year, read = row.strip().split(",")
            print(f"{name} by {author} ({year}) {read}")


def search_book():
    keyword = input("Enter book name: ").strip().title()
    with open(DAY14) as book:
        books = book.readlines()
    c = False
    for book in books:
        name, author, year, read = book.strip().split(",")
        if keyword.lower() in name.lower():
            print(f"{name} by {author} ({year}) {read}")
            c = True
    if not c:
        print("No such book match the keyword")


def mark_book():
    book_title = input("Enter book title: ").strip()
    with open(DAY14) as book:
        books = book.readlines()
    with open(DAY14, 'w') as f:
        c = True
        for book in books:
            name, author, year, read = book.strip().split(",")
            if c and book_title.lower() == name.lower():
                f.write(f"{name},{author},{year},Yes\n")
                c = False
            else:
                f.write(f"{name},{author},{year},{read}\n")


def delete_book():
    book_title = input("Enter book title: ").strip()
    with open(DAY14) as book:
        books = book.readlines()
    with open(DAY14, 'w') as f:
        c = True
        for book in books:
            name, author, year, read = book.strip().split(",")
            if book_title.lower() != name.lower():
                f.write(f"{name},{author},{year},{read}\n")
            else:
                if c:
                    c = False
                else:
                    f.write(f"{name},{author},{year},{read}\n")

        

while True:
    try:
        with open(FILE_NAME, "x") as f:
            pass
    except:
        pass

    choice = input(menu).strip().lower()
    if choice == 'a':
        add_book()
    elif choice == 'r':
        retrive_books()
    elif choice == 's':
        search_book()
    elif choice == 'm':
        mark_book()
    elif choice == 'd':
        delete_book()
    elif choice == 'q':
        print("Quitting the menu")
        break
    else:
        print("Invalid input")
