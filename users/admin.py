from django.contrib import admin
from .models import UserInformation


class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'delivery_address')
    search_fields = ('name', 'delivery_address')
    list_filter = ('name', 'delivery_address')


admin.site.register(UserInformation, UserInformationAdmin)
