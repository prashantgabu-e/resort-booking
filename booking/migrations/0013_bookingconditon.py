# Generated by Django 4.2.1 on 2023-09-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_remove_roombooking_age_roombooking_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingConditon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.TextField()),
                ('condition_arabic', models.TextField()),
                ('sequence', models.SmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Booking Conditions',
                'verbose_name_plural': 'Booking Conditions',
                'ordering': ['sequence'],
            },
        ),
    ]
