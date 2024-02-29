book = input()
number_books = 0

while True:
    name = input()

    if book == name:
        print(f'You checked {number_books} books and found it.')
        break

    if name == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {number_books} books.')
        break

    number_books += 1