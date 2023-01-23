from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


# Restaurant Url's


urlpatterns = [
    path('',views.index,name='index'),
    path('<str:restaurant>',views.main,name='main'),
    path('dishes/display',views.dishes_display,name='dishes_display'),
    path('dishes/add',views.add_dishes,name='add_dishes'),
    path('dishes/edit/<int:id>',views.edit_dishes,name='edit_dishes'),
    path('dishes/delete/<int:id>',views.delete_dishes,name='delete_dishes'),
    path('store/open',views.open_store,name='open_store'),
    path('store/close',views.close_store,name='close_store'),
    path('order/view/<int:id>',views.view_items,name='view_items'),
    path('send-api/<int:id>',views.send_api,name='send_api'),
    path('orders/view',views.orders_page,name='orders_page'),
    path('download/orders',views.export_orders_xlsx,name='export_orders_xlsx'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


