# Generated by Django 2.1.5 on 2019-03-04 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='address',
            new_name='cust_address',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='age',
            new_name='cust_age',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='name',
            new_name='cust_name',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='phone_number',
            new_name='cust_phone_number',
        ),
    ]
