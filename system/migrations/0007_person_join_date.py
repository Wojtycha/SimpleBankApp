# Generated by Django 3.0.4 on 2020-03-11 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_remove_person_join_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='join_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data dołączenia:'),
            preserve_default=False,
        ),
    ]
