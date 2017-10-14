from django.core.serializers import serialize

from .models import ColoringBook


def get_coloring_book(primary_key):
    coloring_book = ColoringBook.objects.get(pk=primary_key)
    return create_coloring_book_dict(coloring_book)


def get_all_books():
    all_books = ColoringBook.objects.all()
    book_dicts = []
    for book in all_books:
        book_dicts.append(create_coloring_book_dict(book))
    return book_dicts


# Creates and returns a json object representing that can be
# used in an html template
def create_coloring_book_dict(coloring_book):
    return {
        'id': coloring_book.id,
        'title': coloring_book.title,
        'description': coloring_book.description,
        'image_name': coloring_book.image_name,
        'pub_date': coloring_book.pub_date,
        'price': coloring_book.price
    }
