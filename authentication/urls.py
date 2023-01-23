from django.urls import path
from . import views


# Authentication Url's


urlpatterns = [
    path('register/<str:kind>/<int:id>',views.register,name='register'),
    path('login/<str:kind>/<int:id>',views.login,name='login'),
    path('logout/<str:kind>',views.logout,name='logout'),
    path('logout-register/<str:kind>/<int:id>',views.logout_register,name='logout_register'),
]


