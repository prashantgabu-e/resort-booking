# Generated by Django 4.2.1 on 2023-07-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0006_roombooking_booking_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="hall_capacity",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="room",
            name="no_of_bathroom",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="room",
            name="no_of_bedroom",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="room",
            name="no_of_hall",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="room",
            name="no_of_swimming_pool",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="room",
            name="size_of_restroom",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Enter in meter(s)",
                max_digits=20,
            ),
        ),
    ]
