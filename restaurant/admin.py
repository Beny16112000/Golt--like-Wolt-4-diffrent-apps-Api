from django.contrib import admin
from .models import Restaurant, Location, Dishes, Open


# Register your models here.


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','category')
admin.site.register(Restaurant, RestaurantAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location',)
admin.site.register(Location, LocationAdmin)


class DishesAdmin(admin.ModelAdmin):
    list_display = ('restaurant','name','price')
admin.site.register(Dishes, DishesAdmin)


class OpenAdmin(admin.ModelAdmin):
    list_display = ('restaurant','available')
admin.site.register(Open, OpenAdmin)


