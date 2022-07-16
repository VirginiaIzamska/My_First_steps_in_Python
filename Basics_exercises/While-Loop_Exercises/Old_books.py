book = input()


count_books = 0
current_book = ""
while current_book != 'No More Books':
    current_book = input()
    if book == current_book:
        print(f"You checked {count_books} books and found it.")
        break
    if current_book != 'No More Books':
        count_books += 1
if current_book != book:
    print(f"The book you search is not here!")
    print(f"You checked {count_books} books.")
