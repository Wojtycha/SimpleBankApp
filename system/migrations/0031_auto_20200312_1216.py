# Generated by Django 3.0.4 on 2020-03-12 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0030_auto_20200312_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klienci',
            name='Status',
        ),
        migrations.RemoveField(
            model_name='klienci',
            name='TypKontaktu',
        ),
    ]
