book_title = []
book_author = set()
book_dicts = {}

book_title.append('Programming Language')
book_author.add('James Bond')
book_dicts["Programming Language"] = 'James Bond'

book_title.append('Python')
book_author.add('Alexander Arnold')
book_dicts["Python"] = 'Alexander Arnold'

book_title.append('Java Script')
book_author.add('Jeremy Brown')
book_dicts["Java Script"] = 'Jeremy Brown'

search= input("What book are you searching for?")
if search in book_title:
    print(f"Book Found! Author: {book_dicts[search]} ")
else:
    print("Book not available")

print("Lists of books: ")
for book in book_title:
    print(book)

remove = input("What book do you wish to remove?")
if remove in book_title:
    remove_author= book_dicts[remove]
    book_title.remove(remove)
    book_author.remove(remove_author)
    del book_dicts[remove]
    print("Book removed successfully")
    print("Available books: ", book_title)
else:
    print("Book not found!")