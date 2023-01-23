from ..models import CustomUser
from django.contrib.auth import authenticate, login, logout


# User Class


class Userclass:

    def create(self, username, email, fname, lname, password, kind):
        myuser = CustomUser.objects.create(username=username, email=email, first_name=fname, last_name=lname, password=password, kind=kind, is_active=False)
        myuser.save()
        return True


    def sign_in(self, username, password, request):
        user = CustomUser.objects.get(username=username)
        user.is_active = True
        user.save()
        login(request, user)
        return True

    
    def sign_out(self, request):
        logout(request)
        return True


