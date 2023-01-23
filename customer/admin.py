from django.contrib import admin
from .models import OrderItems, Order, Rating


# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','paid_status')
admin.site.register(Order, OrderAdmin)


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('user','order')
admin.site.register(OrderItems, OrderItemsAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user','restaurant','rate')
admin.site.register(Rating, RatingAdmin)


