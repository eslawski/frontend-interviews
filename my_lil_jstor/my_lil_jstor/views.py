from django.shortcuts import get_object_or_404, render

from .models import ColoringBook

def coloring_books(request, book_id):
    book = get_object_or_404(ColoringBook, pk=book_id)
    context = {
        'book': book
    }

    return render(request, 'coloring_book_view.html', context)