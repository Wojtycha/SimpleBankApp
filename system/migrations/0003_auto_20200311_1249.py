# Generated by Django 3.0.4 on 2020-03-11 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_person_join_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Name',
            new_name='Imie',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='Surname',
            new_name='Nazwisko',
        ),
    ]
