from django.core.serializers import serialize

from .models import ColoringBook


def get_coloring_book(primary_key):
    coloring_book = ColoringBook.objects.get(pk=primary_key)
    coloring_book_dict = {
        'title': coloring_book.title,
        'description': coloring_book.description,
        'image_name': coloring_book.image_name,
        'pub_date': coloring_book.pub_date
    }

    return coloring_book_dict
