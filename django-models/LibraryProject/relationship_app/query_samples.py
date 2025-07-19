import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()


from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
print(f"\n Books by {author.name}:")
for book in books_by_author:
    print("-", book.title)

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)

books_in_library = library.books.all()
print(f"\n Books in {library.name}:")
for book in books_in_library:
    print("-", book.title)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\n ‍ Librarian of {library.name} is {librarian.name}")

