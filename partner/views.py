from django.shortcuts import render, HttpResponse, redirect
from .models import Partner, Delivery
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json
from customer.models import Order


# Create your views here.


def index(request):
    """
    Handle partner enter's
    """
    if request.user.is_authenticated:
        if request.user.kind == 'partner':
            try:
                Partner.objects.get(user=request.user)
                return redirect('/partner/main')
            except ObjectDoesNotExist:
                create = Partner.objects.create(user=request.user)
                create.save()
                return redirect('/partner/main')
        else:
            return render(request, 'partner/logout.html')
    else:
        return redirect('/auth/login/partner/3')



def main(request):
    """
    Main page or view orders
    """
    partner = Partner.objects.get(user=request.user)
    orders = Delivery.objects.filter(partner=partner,delivered=False)
    return render(request, 'partner/main.html', {'partner': partner, 'orders': orders})



def online(request):
    """
    Go online
    """
    partner = Partner.objects.get(user=request.user)
    partner.available = True
    partner.save()
    return redirect('/partner/main')



def offline(request):
    """
    Go offline
    """
    partner = Partner.objects.get(user=request.user)
    partner.available = False
    partner.save()
    return redirect('/partner/main')



@csrf_exempt
def get_delivery(request):
    """
    Get Delivery
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        partner = Partner.objects.filter(available=True)
        order = Order.objects.get(id=data['id'])
        delivery = Delivery.objects.create(partner=partner[0],order=order,on_way=True)
        delivery.save()
        order.ready = True
        order.save()
        return redirect('/partner/')



def delivered(request, id):
    """
    Delivered function
    """
    order = Order.objects.get(id=id)
    order.delivered = True
    order.save()
    delivery = Delivery.objects.get(order=order)
    delivery.delivered = True
    delivery.save()
    return redirect('/partner/main')



def order_page(request):
    """
    Delivered Orders of partner
    """
    partner = Partner.objects.get(user=request.user)
    orders = Delivery.objects.filter(partner=partner)
    salary = len(orders) * 20
    return render(request, 'partner/orders.html', {'orders': orders, 'salary': salary})


