from django.contrib import admin
from .models import *

#=======================Room Feature==========================#

class RoomFeatureAdmin(admin.ModelAdmin):
    change_form_template = 'admin/roomfeature/change_form.html'
    
#=======================Home Page Banner==========================#
 
class BannerImageInline(admin.TabularInline):
    model = BannerImage
    extra = 1


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    inlines = [BannerImageInline]


@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_editable = ('is_approved',)
    list_display = ('booking_id', 'user', 'selected_date', 'booking_date', 'total_price', 'is_approved')



# admin.site.register(Banner, BannerAdmin)
admin.site.register(RoomBanner)
admin.site.register(ContactUsBanner)
admin.site.register(ContactDetails)
admin.site.register(ContactForm)
admin.site.register(RoomFeature, RoomFeatureAdmin)
admin.site.register(Room)
admin.site.register(RoomPrice)


