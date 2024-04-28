def add_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")
    else:
        print(f"Book '{title}' by {author} already exists in the library.")
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_book(library, "To Kill a Mockingbird", "Harper Lee")
add_book(library, "The Catcher in the Rye", "J.D. Salinger")
add_book(library, "The Great Gatsby", "F. Scott Fitzgerald")

print("\nUpdated Library:")
for i, book in enumerate(library, 1):
    title, author = book
    print(f"{i}. '{title}' by {author}")
