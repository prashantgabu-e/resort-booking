# Generated by Django 4.2.1 on 2023-07-20 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_remove_contactdetails_email_arabic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='email_arabic',
        ),
        migrations.RemoveField(
            model_name='contactform',
            name='message_arabic',
        ),
        migrations.RemoveField(
            model_name='contactform',
            name='name_arabic',
        ),
        migrations.RemoveField(
            model_name='contactform',
            name='phone_number_arabic',
        ),
    ]
