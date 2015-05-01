# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='ID',
            new_name='book_id',
        ),
    ]
