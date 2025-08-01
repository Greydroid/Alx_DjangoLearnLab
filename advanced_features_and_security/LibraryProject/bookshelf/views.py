from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})



from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.db.models import Q

# ✅ Example: Safe search view
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )
    return render(request, 'bookshelf/book_list.html', {'books': books})

# ✅ Example: Safe form handling
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # ✅ Validates user input
            form.save()
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

