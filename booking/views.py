import datetime
from dateutil.parser import parse

from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from . import helper
from .models import *
from .choices import MyChoice



def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect("home-page")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


def home(request):
    banners = Banner.objects.prefetch_related("images").all()
    room = Room.objects.all().first()
    room_banner = RoomBanner.objects.all()
    context = {
        "banners": banners,
        "room": room,
        "room_banner": room_banner,
    }
    return render(request, "home.html", context)


def calendar(request, pk):
    room_price_list = []
    dates_with_price = []
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year

    room = Room.objects.filter(id=pk).first()
    filter_q = Q(start_date__month=current_month, start_date__year=current_year) | Q(
        end_date__month=current_month, end_date__year=current_year
    )
    room_prices_qs = room.room_price.filter(filter_q).order_by("start_date")
    all_room_booking = room.room_booking.filter(
        selected_date__month=current_month, selected_date__year=current_year
    )
    for room_price in room_prices_qs:
        dates_with_price = helper.get_dates_between(
            room_price.start_date, room_price.end_date
        )
        for date_with_price in dates_with_price:
            is_room_available = True
            room_booking_count = all_room_booking.filter(
                is_approved=True, selected_date=parse(date_with_price)
            ).count()
            if room_booking_count >= 4:
                is_room_available = False
            title = None
            if room_price.special_price:
                title = f"<s>{room_price.price}SR</s></br>{room_price.special_price}SR"
            else:
                title = f"{room_price.price}SR"

            room_price_data = {
                "start": date_with_price,
                "rate": room_price.price,
                "is_room_available": f"{is_room_available}",
                "title": title
                if is_room_available
                else "Not Available",
            }
            if not is_room_available:
                room_price_data["color"] = "red"
            room_price_list.append(room_price_data)
    context = {
        "room_prices": room_price_list, 
        "room_id": pk
    }
    return render(request, "calendar.html", context)


def restroom(request):
    banners = RoomBanner.objects.all()
    room_feature = RoomFeature.objects.all()
    room = Room.objects.all()
    contacts_details = ContactDetails.objects.only("phone_number")

    if request.method == "POST":
        # Process the form data and create a RoomBooking object
        name = request.POST.get("name")
        number = request.POST.get("phone_number")
        age = request.POST.get("age")
        id_number = request.POST.get("id_number")
        special_requests = request.POST.get("special_requests")

        total_price = request.POST.get("total_price")
        selected_dates = request.POST.get("selected_dates")
        room_id = request.POST.get("room_id")

        room_booking = RoomBooking(
            name=name,
            number=number,
            age=age,
            id_number=id_number,
            special_requests=special_requests,
            selected_date=parse(selected_dates),
            user=request.user if not request.user.is_anonymous else None,
            total_price=total_price,
            selected_dates=selected_dates,
            room_id=room_id,
        )
        room_booking.save()

        subject = "New Booking Request"
        message = f"Booking ID: #{room_booking.booking_id} \n\nCustomer Details: \nName: {name}\nPhone number: {number}\nAge: {room_booking.age} \n\nBooking Date: {room_booking.booking_date}\nCheck In: {room_booking.selected_date.date()}\nPrice: {room_booking.total_price}\n\nId Number: {room_booking.id_number}\nSpecial Requests: {room_booking.special_requests}"
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            import traceback
            print(traceback.format_exc())

        return redirect(
            reverse("congrats-page") + f"?room_id={room_booking.booking_id}"
        )

    # Get the room information
    room_id = request.GET.get("room_id")
    if room_id:
        room = Room.objects.get(id=room_id)
    else:
        None

    context = {
        "banners": banners,
        "rooms": room,
        "room_feature": room_feature,
        "contacts_details": contacts_details,
        "room": room,
    }

    return render(request, "restroom.html", context)


def congrats_page(request):
    booking_id = request.GET.get("room_id")
    hero = Congratulation.objects.all().first()
    booking_details = None
    check_in_date = None

    if booking_id:
        booking_details = RoomBooking.objects.filter(booking_id=int(booking_id))
        booking_details_obj = booking_details.first()
        if booking_details_obj.selected_dates:
            check_in_date = parse(booking_details_obj.selected_dates)
    context = {"booking_details": booking_details, "check_in_date": check_in_date, "hero": hero}
    return render(request, "congratulations.html", context)


def get_month_start_end_dates(year, month):
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])
    return first_day, last_day


def room_price_calendar_api(request):
    from dateutil.parser import parse

    room_id = request.GET.get("room")
    start_date_str = request.GET.get("start_date")
    start_date = parse(start_date_str)
    room_price_list = []
    dates_with_price = []
    current_month = start_date.month
    current_year = start_date.year

    room = Room.objects.filter(id=int(room_id)).first()
    filter_q = Q(start_date__month=current_month, start_date__year=current_year) | Q(
        end_date__month=current_month, end_date__year=current_year
    )
    room_prices_qs = room.room_price.filter(filter_q).order_by("start_date")
    all_room_booking = room.room_booking.filter(
        selected_date__month=current_month, selected_date__year=current_year
    )
    for room_price in room_prices_qs:
        dates_with_price = helper.get_dates_between(
            room_price.start_date, room_price.end_date
        )
        for date_with_price in dates_with_price:
            is_room_available = True
            title = None
            if room_price.special_price:
                title = f"<s>{room_price.price}SR</s></br>{room_price.special_price}SR"
            else:
                title = f"{room_price.price}SR"

            room_booking_count = all_room_booking.filter(
                is_approved=True, selected_date=parse(date_with_price)
            ).count()
            if room_booking_count >= 4:
                is_room_available = False
            room_price_data = {
                "start": date_with_price,
                "rate": room_price.price,
                "is_room_available": f"{is_room_available}",
                "title": title
                if is_room_available
                else "Not Available",
            }
            if not is_room_available:
                room_price_data["color"] = "red"
            room_price_list.append(room_price_data)
    return JsonResponse(room_price_list, safe=False)


def contact(request):
    contacts_details = ContactDetails.objects.all()
    context = {"contacts_details": contacts_details}
    return render(request, "contact.html", context)


def submit_contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")

        contact_form = ContactForm(
            name=name, email=email, phone_number=phone_number, message=message
        )
        contact_form.save()

        return redirect(reverse("home-page"))
    # If the request method is not POST, render the form again.
    return render(request, "contact.html")


@login_required(login_url="/login")
def booking_list(request):
    bookings = RoomBooking.objects.filter(user=request.user).order_by("-id")
    paginator = Paginator(bookings, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "booking_list.html", {"page_obj": page_obj})
