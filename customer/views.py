from django.shortcuts import render, HttpResponse, redirect
from restaurant.models import Restaurant, Dishes, Location, Open
from .models import OrderItems, Order, Rating
from django.contrib import messages
from .api.request import ApiClass
from django.middleware.csrf import get_token
from django.db.models import Avg
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def index(request):
    """
    Handle customer enter's
    """
    if request.user.is_authenticated:
        if request.user.kind == 'customer':
            return redirect('/customer/main')
        else:
            return render(request, 'customer/logout.html')
    else:
        return redirect('/auth/login/customer/2')



def main(request):
    """
    Main page
    """
    restaurants = Open.objects.filter(available=True)
    return render(request, 'customer/main.html', {'restaurants': restaurants})


   
def restaurant_page(request, id):
    """
    Restaurant page display + add to cart
    """
    restaurant = Restaurant.objects.get(id=id)
    dishes = Dishes.objects.filter(restaurant=restaurant)
    if request.method == 'POST':
        dish = request.POST['dish']
        get_dish = Dishes.objects.get(id=dish)
        items = OrderItems.objects.create(user=request.user,restaurant=restaurant,
                                            dish=get_dish)
        items.save()
        messages.success(request, 'Added To cart')
        return render(request, 'customer/restaurant.html', {'restaurant': restaurant, 'dishes': dishes})      
    return render(request, 'customer/restaurant.html', {'restaurant': restaurant, 'dishes': dishes})



def cart(request):
    """
    Cart Page
    """
    total = 0
    items = OrderItems.objects.filter(user=request.user,paid_status=False)
    for i in items:
        total += int(i.dish.price)
    return render(request, 'customer/cart.html', {'items': items, 'total': total})



def checkout(request):
    """
    Checkout Page
    """
    total = 0
    location = Location.objects.all()
    if request.method == 'POST':
        phone = request.POST['phone']
        adress = request.POST['location']
        find_total = OrderItems.objects.filter(user=request.user,paid_status=False)
        for i in find_total:
            total += int(i.dish.price)
        if total == 0:
            return redirect('/customer/main') 
        restaurant = Restaurant.objects.get(id=find_total[0].restaurant.id)
        locate = Location.objects.get(id=adress)
        order = Order.objects.create(user=request.user,restaurant=restaurant,total=total,
                                    paid_status=True,location=locate,phone=phone)
        order.save()
        last_order = Order.objects.last()
        OrderItems.objects.filter(user=request.user,paid_status=False).update(order=last_order.id,paid_status=True)
        token = get_token(request)
        api = ApiClass(restaurant.name,last_order.id,token).restaurantOrder()
        if api == 200:
            return redirect(f'/customer/main/orders/{last_order.id}')
        else:
            messages.error(request, 'Field')
            return render(request, 'customer/checkout.html', {'location': location})
    return render(request, 'customer/checkout.html', {'location': location})



def delete_item(request, id):
    """
    Delete item from cart
    """
    item = OrderItems.objects.get(id=id)
    item.delete()
    return redirect('/customer/cart')



def orders_page(request):
    """
    Orders Page
    """
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'customer/orders.html', {'orders': orders})



def single_order(request, id):
    """
    Single order Page
    """
    order = Order.objects.get(id=id)
    items = OrderItems.objects.filter(order=order)
    try:
        rating = Rating.objects.get(user=request.user,order=order)
    except ObjectDoesNotExist:
        rating = None
    return render(request, 'customer/single_order.html', {'order': order, 'items': items, 'rating': rating})



def search(request):
    """
    Search page result
    """
    q = request.GET['q']
    restaurants = Restaurant.objects.filter(category=q)
    return render(request, 'customer/search.html', {'q': q, 'restaurants': restaurants})



def restaurant_detail(request, name):
    """
    Restaurant detail page
    """
    restaurant = Restaurant.objects.get(name=name)
    rating = Rating.objects.filter(restaurant=restaurant).aggregate(Avg('rate'))
    return render(request, 'customer/restaurant_detail.html', {'restaurant': restaurant, 'avg': rating})



def rate(request, id):
    """
    Rate restautant after delivery done
    """
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        num = request.POST['rating']
        rating = Rating.objects.create(user=request.user,restaurant=order.restaurant
                                        ,order=order,rate=num)
        rating.save()
        return redirect('/customer/main/orders')
    return render(request, 'customer/rating.html', {'order': order})


