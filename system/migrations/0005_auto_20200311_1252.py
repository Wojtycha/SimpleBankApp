# Generated by Django 3.0.4 on 2020-03-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20200311_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
