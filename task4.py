library_books = {
    "The Great Gatsby": True,
    "1984": False,
    "Moby Dick": True,
    "To Kill a Mockingbird": False
}

while True:
    book_name = input("Enter the name of book, for exit press 0: ")
    if book_name == "0":
        print("Exiting...")
        break

    book_found = False

    for book in library_books:
        if book_name == book:
            book_found = True
            if library_books[book]:
                library_books[book] = False
                print("The book is available, it is checked out successfully.\n")
            else:
                print(f"{book_name} is already checked out, the checkout request is denied.\n")
            break

    if not book_found:
        print("Book not found in the library.\n")
