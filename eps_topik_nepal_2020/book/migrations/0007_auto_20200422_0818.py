# Generated by Django 3.0.5 on 2020-04-22 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_audiomp3file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiomp3file',
            old_name='book',
            new_name='book_chapter',
        ),
    ]
