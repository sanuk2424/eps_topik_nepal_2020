# Generated by Django 3.0.5 on 2020-04-22 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_delete_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioMp3File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp3_file', models.FileField(default='', upload_to='book/mp3')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
    ]
