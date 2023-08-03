from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.utils.translation import gettext as _

from dateutil.parser import parse

class Banner(models.Model):
    title = models.CharField(max_length=100)
    title_arabic = models.CharField(max_length=100)
    description = models.TextField()
    description_arabic = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')

class BannerImage(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name="images")
    image = models.FileField(upload_to="banners/")

    def __str__(self):
        return self.image.name
    
    class Meta:
        verbose_name = _('Banner Image')
        verbose_name_plural = _('Banner Images')


class RoomBanner(models.Model):
    image = models.FileField(upload_to="banners/")

    def __str__(self) -> str:
        return self.image.name


    class Meta:
        verbose_name = _('Room Banner')
        verbose_name_plural = _('Room Banners')

class ContactUsBanner(models.Model):
    image = models.FileField(upload_to="banners/")

    def __str__(self) -> str:
        return self.image.name


    class Meta:
        verbose_name = _('Contact Us Banner')
        verbose_name_plural = _('Contact Us Banners')


class ContactDetails(models.Model):
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    fax = models.CharField(max_length=20, null=True, blank=True)
    google_map_link = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    address_arabic = models.TextField()
    description_arabic = models.TextField(null=True, blank=True)

    google_map_link = models.CharField(max_length=500)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    snapchat = models.URLField(null=True, blank=True)
    tiktok = models.URLField(null=True, blank=True)



    def __str__(self) -> str:
        return f"{self.email} and {self.phone_number}"


    class Meta:
        verbose_name = _('Contact Details')
        verbose_name_plural = _('Contact Details')


    def save(self, *args, **kwargs):
        if not self.pk and ContactDetails.objects.exists():
            raise ValidationError("Only one ContactDetails object can be created.")
        return super().save(*args, **kwargs)


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.email} and {self.phone_number}"


    class Meta:
        verbose_name = _('Contact Form')
        verbose_name_plural = _('Contact Forms')

class RoomFeature(models.Model):
    feature_name = models.CharField(max_length=40)
    feature_name_arabic = models.CharField(max_length=40)
    icon_class = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.feature_name


    class Meta:
        verbose_name = _('Room Feature')
        verbose_name_plural = _('Room Features')

class Room(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    name_arabic = models.CharField(max_length=50)
    location_arabic = models.CharField(max_length=100)
    description_arabic = models.TextField()
    allow_people = models.IntegerField()
    feature = models.ManyToManyField(RoomFeature)
    size_of_restroom = models.DecimalField(
        max_digits=20, default=0, decimal_places=2, help_text="Enter in meter(s)"
    )
    room_image = models.FileField(upload_to="room_images/", null=True, blank=True)
    no_of_swimming_pool = models.IntegerField(default=0)
    no_of_bathroom = models.IntegerField(default=0)
    no_of_bedroom = models.IntegerField(default=0)
    no_of_hall = models.IntegerField(default=0)
    hall_capacity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')

class RoomPrice(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_price")
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.room.name} - {self.start_date} to {self.end_date}"

    class Meta:
        verbose_name = _('Room Price')
        verbose_name_plural = _('Room Prices')


class RoomBooking(models.Model):
    booking_id = models.CharField(max_length=4, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="room_booking"
    )
    is_approved = models.BooleanField(default=False)
    selected_dates = models.CharField(max_length=100, null=True, blank=True)
    selected_date = models.DateField(null=True, blank=True)
    booking_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.room.name} - {self.booking_date}"


    class Meta:
        verbose_name = _('Room Booking')
        verbose_name_plural = _('Room Bookings')


    @property
    def check_in_date(self):
        check_in_date = None
        if self.selected_dates:
            check_in_date = parse(self.selected_dates)
        return check_in_date


    def save(self, *args, **kwargs):
        if not self.booking_id:
            # Generate the next booking ID based on existing bookings for the room
            last_booking = (
                RoomBooking.objects.filter(room=self.room)
                .order_by("-booking_id")
                .first()
            )

            if last_booking and last_booking.booking_id:
                last_booking_id = int(last_booking.booking_id)
                new_booking_id = str(last_booking_id + 1).zfill(4)
            else:
                new_booking_id = "1000"

            self.booking_id = new_booking_id

        super().save(*args, **kwargs)
