# Generated by Django 4.2.1 on 2023-09-10 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_roomfeature_sequence'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomfeature',
            options={'ordering': ['sequence'], 'verbose_name': 'Room Feature', 'verbose_name_plural': 'Room Features'},
        ),
    ]