# Generated by Django 2.1.5 on 2019-03-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20190228_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_delete',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
