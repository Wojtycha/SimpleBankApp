# Generated by Django 3.0.4 on 2020-03-11 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0017_auto_20200311_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='join_date',
            field=models.DateField(default=datetime.date.today, editable=False, verbose_name='Data dołączenia'),
        ),
    ]
