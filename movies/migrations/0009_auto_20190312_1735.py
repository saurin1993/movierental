# Generated by Django 2.1.5 on 2019-03-13 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_movies_movie_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='movie_delete',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='movie_update',
        ),
    ]
