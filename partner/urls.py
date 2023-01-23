from django.urls import path
from . import views


# Partner Url's


urlpatterns = [
    path('',views.index,name="index"),
    path('main',views.main,name='main'),
    path('main/available/online',views.online,name='online'),
    path('main/available/offline',views.offline,name='offline'),
    path('get-api',views.get_delivery,name='get_delivery'),
    path('delivered/<int:id>',views.delivered,name='delivered'),
    path('orders/view',views.order_page,name='order_page'),
]


