from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.i18n import i18n_patterns

from booking import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    # my-views
    # path("", views.home, name="home-page"),
    # path("calendar/<int:pk>/", views.calendar, name="calendar-page"),
    # path("restroom", views.restroom, name="restroom-page"),
    # path("contact-us", views.contact, name="contact-page"),
    # path("contact-form/submit/", views.submit_contact_form, name="contact-form-submit"),
    # path("bookings/", views.booking_list, name="booking-list"),
    # path("congrats/", views.congrats_page, name="congrats-page"),

]

urlpatterns += [path('i18n/', include('django.conf.urls.i18n')), ]
urlpatterns += i18n_patterns(path('admin/', admin.site.urls), prefix_default_language=False)
# urlpatterns += i18n_patterns(path("", views.home, name="home-page"))
urlpatterns += i18n_patterns(
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_view, name="register-page"),
    path("", views.home, name="home-page"),
    path("calendar/<int:pk>/", views.calendar, name="calendar-page"),
    path("contact-us", views.contact, name="contact-page"),
    path("contact-form/submit/", views.submit_contact_form, name="contact-form-submit"),
    path("bookings/", views.booking_list, name="booking-list"),
    path("restroom", views.restroom, name="restroom-page"),
    path("congrats/", views.congrats_page, name="congrats-page"),
        path(
        "api/room/price/calendar/",
        views.room_price_calendar_api,
        name="room_price_calendar_api",
    ),prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
