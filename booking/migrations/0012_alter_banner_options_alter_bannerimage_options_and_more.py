# Generated by Django 4.2.1 on 2023-07-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0011_remove_contactdetails_email_arabic_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="banner",
            options={"verbose_name": "صفحة", "verbose_name_plural": "صفحات"},
        ),
        migrations.AlterModelOptions(
            name="bannerimage",
            options={"verbose_name": "صفحة الصور", "verbose_name_plural": "صفحة الصور"},
        ),
        migrations.AlterModelOptions(
            name="contactdetails",
            options={
                "verbose_name": "معلومات التواصل",
                "verbose_name_plural": "معلومات التواصل",
            },
        ),
        migrations.AlterModelOptions(
            name="contactform",
            options={
                "verbose_name": "نموذج التواصل",
                "verbose_name_plural": "تماذج التواصل",
            },
        ),
        migrations.AlterModelOptions(
            name="contactusbanner",
            options={"verbose_name": "تواصل معنا", "verbose_name_plural": "تواصل معنا"},
        ),
        migrations.AlterModelOptions(
            name="room",
            options={"verbose_name": "غرفة", "verbose_name_plural": "غرف"},
        ),
        migrations.AlterModelOptions(
            name="roombanner",
            options={
                "verbose_name": "صفحة الغرفة",
                "verbose_name_plural": "صفحة الغرفة",
            },
        ),
        migrations.AlterModelOptions(
            name="roombooking",
            options={"verbose_name": "حجز غرفة", "verbose_name_plural": "حجوزات الغرف"},
        ),
        migrations.AlterModelOptions(
            name="roomfeature",
            options={
                "verbose_name": "مميزة الغرفة",
                "verbose_name_plural": "مميزات الغرف",
            },
        ),
        migrations.AlterModelOptions(
            name="roomprice",
            options={
                "verbose_name": "سعر الغرفة",
                "verbose_name_plural": "اسعار الغرف",
            },
        ),
        migrations.RemoveField(
            model_name="contactform",
            name="email_arabic",
        ),
        migrations.RemoveField(
            model_name="contactform",
            name="message_arabic",
        ),
        migrations.RemoveField(
            model_name="contactform",
            name="name_arabic",
        ),
        migrations.RemoveField(
            model_name="contactform",
            name="phone_number_arabic",
        ),
        migrations.AddField(
            model_name="roombooking",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
    ]
