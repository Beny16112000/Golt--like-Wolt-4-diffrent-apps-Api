from django.urls import path
from . import views


# Customer Url's


urlpatterns = [
    path('',views.index,name='index'),
    path('main',views.main,name='main'),
    path('main/<int:id>',views.restaurant_page,name='restaurant_page'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('delete/item/<int:id>',views.delete_item,name='delete_item'),
    path('main/orders',views.orders_page,name='orders_page'),
    path('main/orders/<int:id>',views.single_order,name='single_order'),
    path('main/search-result/',views.search,name='search'),
    path('main/restaurant/<str:name>',views.restaurant_detail,name='restaurant_detail'),
    path('main/orders/rate/<int:id>',views.rate,name='rate'),
]


