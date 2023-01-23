from django.shortcuts import render, HttpResponse, redirect
from .models import Restaurant, Location, Dishes, Open
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from customer.models import Order, OrderItems, Rating
from .api.api import Api
from django.middleware.csrf import get_token
from django.db.models import Avg, Sum
from openpyxl import Workbook


# Create your views here.


def index(request):
    """
    Handle Cient enter to the restaurant path
    """
    if request.user.is_authenticated:
        try:
            restaurant = Restaurant.objects.get(user=request.user)
            return redirect(f'/restaurant/{restaurant.name}')
        except ObjectDoesNotExist:
            pass
        if request.method == 'POST' and request.FILES['img']:
            name = request.POST['name']
            loc = request.POST['location']
            category = request.POST['category']
            img = request.FILES['img']
            url = request.POST['url']
            detail = request.POST['detail']
            location_instance = Location.objects.get(id=loc)
            save = Restaurant.objects.create(user=request.user,name=name,location=location_instance,
                                            img=img,category=category,detail=detail,website=url)
            save.save()
            restaurant_last = Restaurant.objects.last()
            save_open = Open.objects.create(restaurant=restaurant_last)
            save_open.save()
            return redirect(f'/restaurant/{name}')
        location = Location.objects.all()
        return render(request, 'restaurant/register.html', {'location':location})
    else:
        return redirect('/auth/login/restaurant/1')


@csrf_exempt
def main(request, restaurant, **kwargs):
    """
    Main page of restaurant
    """
    get_restaurant = Restaurant.objects.get(name=restaurant)
    orders = Order.objects.filter(restaurant=get_restaurant,ready=False)
    available = Open.objects.get(restaurant=get_restaurant)
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.get(id=data['id'])
        item = OrderItems.objects.filter(order=order)
        return redirect(f'/restaurant/{get_restaurant.name}')
    return render(request, 'restaurant/main.html', {'available': available, 'orders':orders})



def dishes_display(request):
    """
    Display your Dishes
    """
    restaurant = Restaurant.objects.get(user=request.user)
    dishes = Dishes.objects.filter(restaurant=restaurant).order_by('id')
    return render(request, 'restaurant/display_dishes.html',{'dishes': dishes})



def add_dishes(request):
    """
    Add dishes
    """
    if request.method == 'POST' and request.FILES['img']:
        name = request.POST['name']
        img = request.FILES['img']
        detail = request.POST['detail']
        price = request.POST['price']
        restaurant = Restaurant.objects.get(user=request.user)
        dishes_save = Dishes.objects.create(restaurant=restaurant,name=name,
                                            img=img,detail=detail,price=price)
        dishes_save.save()
        return redirect('/restaurant/dishes/display')
    return render(request, 'restaurant/add_dishes.html')



def edit_dishes(request, id):
    """
    Edit Dishes
    """
    if request.method == 'POST' and request.FILES['img']:
        name = request.POST['name']
        img = request.FILES['img']
        detail = request.POST['detail']
        price = request.POST['price']
        Dishes.objects.filter(id=id).update(name=name,img=img,
                                            detail=detail,price=price)
        return redirect('/restaurant/dishes/display')
    try:
        dish = Dishes.objects.get(id=id)
        return render(request, 'restaurant/edit_dishes.html', {'dish': dish})
    except ObjectDoesNotExist:
        messages.error(request, 'Not exist !')



def delete_dishes(request, id):
    """
    Delete Dishes
    """
    dish = Dishes.objects.get(id=id)
    dish.delete()
    return redirect('/restaurant/dishes/display')



def open_store(request):
    """
    Open Store
    """
    restaurant = Restaurant.objects.get(user=request.user)
    store = Open.objects.get(restaurant=restaurant)
    store.available = True
    store.save()
    return redirect(f'/restaurant/{restaurant.name}')



def close_store(request):
    """
    Close Store
    """
    restaurant = Restaurant.objects.get(user=request.user)
    store = Open.objects.get(restaurant=restaurant)
    store.available = False
    store.save()
    return redirect(f'/restaurant/{restaurant.name}')



def view_items(request, id):
    """
    View items in order
    """
    order = Order.objects.get(id=id)
    items = OrderItems.objects.filter(order=order)
    return render(request, 'restaurant/order_detail.html', {'items': items, 'order':order})



def send_api(request, id):
    """
    Send ready order
    """
    token = get_token(request)
    api = Api(id, token).partnerOrder()
    return redirect('/restaurant/')



def orders_page(request):
    """
    View Delivered orders
    """
    restaurant = Restaurant.objects.get(user=request.user)
    orders = Order.objects.filter(restaurant=restaurant,delivered=True).order_by('-id')
    orders_sum = orders.aggregate(Sum('total'))
    rating_avg = Rating.objects.filter(restaurant=restaurant).aggregate(Avg('rate'))
    return render(request, 'restaurant/orders.html', {'orders': orders, 'sum': orders_sum, 'avg': rating_avg})



def export_orders_xlsx(request):
    """
    Write Xl file
    """
    restaurant = Restaurant.objects.get(user=request.user)
    orders = Order.objects.filter(restaurant=restaurant)
    wb = Workbook()
    ws = wb.active
    ws.append(['Order ID', 'Customer', 'Total'])
    for order in orders:
        ws.append([order.id, order.user.username, order.total])
    file_name = 'orders.xlsx'
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    wb.save(response)
    return response


