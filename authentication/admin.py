from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username','email','kind')
admin.site.register(CustomUser, CustomUserAdmin)



