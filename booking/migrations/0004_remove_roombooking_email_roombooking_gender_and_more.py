# Generated by Django 4.2.1 on 2023-08-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_banner_options_alter_bannerimage_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roombooking',
            name='email',
        ),
        migrations.AddField(
            model_name='roombooking',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2),
        ),
        migrations.AddField(
            model_name='roombooking',
            name='special_event',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roombooking',
            name='special_requests',
            field=models.TextField(null=True),
        ),
    ]