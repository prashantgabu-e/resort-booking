# Generated by Django 4.2.1 on 2023-09-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_roomfeature_feature_name_arabic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Congratulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.FileField(upload_to='congratulation/')),
                ('title', models.CharField(max_length=100)),
                ('title_arabic', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('description_arabic', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Congratulation',
                'verbose_name_plural': 'Congratulations',
            },
        ),
    ]
