# Create a Book
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

# Output:
# <Book: 1984 by George Orwell (1949)>

# Retrieve the book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Output:
# 1984 George Orwell 1949

# Update the title
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

# Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

# Delete the book
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()

# Output:
# <QuerySet []>

