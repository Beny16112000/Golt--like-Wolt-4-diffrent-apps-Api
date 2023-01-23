from django.contrib import admin
from .models import Partner, Delivery


# Register your models here.


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('user','available')
admin.site.register(Partner, PartnerAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('partner','order')
admin.site.register(Delivery, DeliveryAdmin)


