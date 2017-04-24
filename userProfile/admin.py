from django.contrib import admin

from userProfile.models import BaseCustomUser


class userProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    fields = ['email', 'username', 'first_name', 'middle_name',
                 'last_name', 'gender', 'phone_number', 'birthday', 'address']
admin.site.register(BaseCustomUser, userProfileAdmin)
