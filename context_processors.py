from booking.models import *

def global_context(request):
    # Add the data you want to include in the global context
    data = {
        'contact_details_obj': ContactDetails.objects.filter().first(),
    }
    return data