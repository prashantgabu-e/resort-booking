from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionModelAdmin
from .models import *



#=======================Export Data Resource==========================#
class RoomBookingResource(resources.ModelResource):

    class Meta:
        model = RoomBooking
        # fields = []



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
class RoomBookingAdmin(ExportActionModelAdmin):
    resource_classes = [RoomBookingResource]
    list_editable = ('is_approved',)
    list_display = ('booking_id', 'is_approved', 'number', 'name', 'selected_date', 'booking_date', 'total_price',)


admin.site.register(BannerImage)
admin.site.register(Congratulation)
admin.site.register(RoomBanner)
admin.site.register(ContactUsBanner)
admin.site.register(ContactDetails)
admin.site.register(ContactForm)
admin.site.register(RoomFeature, RoomFeatureAdmin)
admin.site.register(Room)
admin.site.register(RoomPrice)
