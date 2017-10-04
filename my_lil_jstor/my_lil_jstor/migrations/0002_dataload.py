from __future__ import unicode_literals

import json, os

from django.db import migrations


def initial_load(apps, schema_editor):
    ColoringBook = apps.get_model("my_lil_jstor", "ColoringBook")
    with open(os.path.join(os.path.dirname(__file__), 'coloring_books.json')) as data_json:
        coloring_books_json = json.load(data_json)
        for coloring_book in coloring_books_json:
            ColoringBook.objects.create(
                title=coloring_book.get('title'),
                description=coloring_book.get('description'),
                image_name=coloring_book.get('image_name'),
                pub_date=coloring_book.get('pub_date')
            )


class Migration(migrations.Migration):

    dependencies = [
        ('my_lil_jstor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_load),
    ]
