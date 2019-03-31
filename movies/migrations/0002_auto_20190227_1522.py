# Generated by Django 2.1.5 on 2019-02-27 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='category',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='rentedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Movies'),
        ),
    ]