from django.contrib import admin

from .models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "phone_number", "message"]


admin.site.register(Enquiry, EnquiryAdmin)
