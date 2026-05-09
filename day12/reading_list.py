book_list = []
menu = """Enter
'a' - add a book
'd' - display books list
'q' - quit
your choice: """


def add_book():
    book_name = input("Enter book name: ").title().strip()
    book_author = input("Enter book author: ").title().strip()
    year_release = int(input("Enter year released: "))
    book = {
        "name": book_name,
        "author": book_author,
        "year_released": year_release
    }
    book_list.append(book)


def display_books():
    if len(book_list) == 0:
        print("There is no book in book list")
    else:
        # for i in range(len(book_list)):
        for book in book_list:
            name = book["name"]
            author = book["author"]
            year_release = book["year_released"]
            print(f"{name} by {author}, ({year_release})")


while True:
    choice = input(menu).strip().lower()
    if choice == 'a':
        add_book()
    elif choice == 'd':
        display_books()
    elif choice == 'q':
        print("Quitting the menu")
        break
    else:
        print("Invalid input")
