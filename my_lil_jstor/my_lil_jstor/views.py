from django.shortcuts import render
from django.http import JsonResponse
from .services import get_coloring_book
from .services import get_all_books
from .services import like_book


def coloring_books(request, book_id):
    book = get_coloring_book(book_id)
    context = {
        'book': book
    }

    return render(request, 'coloring_book_view.html', context)


def home(request):
    book = get_coloring_book(3)
    context = {
        'book': book
    }

    return render(request, 'home.html', context)


def purchase(request, book_id):
    book = get_coloring_book(book_id)
    context = {
        'book': book
    }
    return render(request, 'purchase.html', context)

# The browse view will show all the books in the system
def browse(request):
    books = get_all_books()
    context = {
        'books': books
    }
    return render(request, 'browse.html', context)

def like(request):
    book_id = request.POST.get('bookId')
    current_likes = like_book(book_id)
    return JsonResponse({
        'likes': current_likes
    })