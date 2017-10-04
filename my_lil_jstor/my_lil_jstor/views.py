from django.shortcuts import get_object_or_404, render

from .services import get_coloring_book


def coloring_books(request, book_id):
    book = get_coloring_book(book_id)
    context = {
        'book': book
    }

    return render(request, 'coloring_book_view.html', context)


def home(request):
    return render(request, 'home.html')