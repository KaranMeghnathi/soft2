from django.shortcuts import render


# Create your views here.

from .models import Kenu, Rest

def home(request):

    kenus = Kenu.objects.all()
    rests = Rest.objects.all()
    return render(request, 'restaurant-menus.html', {'kenus': kenus, 'rests': rests})


def home2(request):
    rests = Rest.objects.all()
    return render(request, 'index.html', {'rests': rests})
