from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from .auth.users import Userclass
from django.contrib.auth.decorators import login_required


# Create your views here.
# Superuser - username: beny, email: b@b.com, password: 1234


def register(request, kind, id):
    """
    Register
    """
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'Password does Not match !')
            return render(request, 'authentication/register.html', {'kind': kind, 'id': id})

        try:
            CustomUser.objects.get(username=username, email=email, kind=kind)
            messages.error(request, 'Username and email need to be uniqe !')
            return render(request, 'authentication/register.html')
        except ObjectDoesNotExist:
            user = Userclass().create(username, email, fname, lname, pass1, kind)
            if user is True:
                return redirect(f'/auth/login/{kind}/{id}')
    return render(request, 'authentication/register.html', {'kind': kind, 'id': id})



def login(request, kind, id):
    """
    Login
    """
    if request.user.is_authenticated:
        return redirect(f'/{kind}')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Userclass().sign_in(username, password, request)
        if user is True:
            return redirect(f'/{kind}')
        else:
            messages.error(request, 'Field to login')
    return render(request, 'authentication/login.html', {'kind': kind, 'id': id})



@login_required
def logout(request, kind):
    """
    Logout
    """
    user = Userclass().sign_out(request)
    if user is True:
        return redirect(f'/{kind}')



def logout_register(request, kind, id):
    """
    Log out and then send to register as kind
    """
    user = Userclass().sign_out(request)
    if user is True:
        return redirect(f'/auth/register/{kind}/{id}')


