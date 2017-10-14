from django.core.serializers import serialize

from .models import ColoringBook, Comment


def get_coloring_book(primary_key):
    coloring_book = ColoringBook.objects.get(pk=primary_key)
    return create_coloring_book_dict(coloring_book)


def get_all_books():
    all_books = ColoringBook.objects.all()
    book_dicts = []
    for book in all_books:
        book_dicts.append(create_coloring_book_dict(book))
    return book_dicts


# Updates the like counter on the provided book and returns the new count
def like_book(primary_key):
    coloring_book = ColoringBook.objects.get(pk=primary_key)
    coloring_book.likes = coloring_book.likes + 1
    coloring_book.save()
    return coloring_book.likes


def insert_comment(user, comment, bookId):
    coloring_book = ColoringBook.objects.get(pk=bookId)
    comment = Comment(user=user, book=coloring_book, comment=comment)
    comment.save()
    return create_comment_dic(comment)


def get_comments(bookId):
    if bookId == "":
        comments = Comment.object.all()
    else:
        comments = Comment.objects.filter(book=bookId)
    sorted_comments = sorted(comments, key=lambda k: k.id, reverse=True)
    comments_dict = []
    for comment in sorted_comments:
        comments_dict.append(create_comment_dic(comment))
    return comments_dict


def create_comment_dic(comment):
    return {
        'user': comment.user,
        'comment': comment.comment
    }

# Creates and returns a json object representing that can be
# used in an html template
def create_coloring_book_dict(coloring_book):
    return {
        'id': coloring_book.id,
        'title': coloring_book.title,
        'description': coloring_book.description,
        'image_name': coloring_book.image_name,
        'pub_date': coloring_book.pub_date,
        'price': coloring_book.price,
        'likes': coloring_book.likes
    }
