from django.shortcuts import render
from .models import  *

# Create your views here.
def home (request):
    home = Bus.objects.all()
    context = {
        'home': home
    }
    return render(request,template_name='bus\home.html',context=context)

def seat (request):
    return render(request,template_name='bus\seat.html')
def info (request):
    return render(request,template_name='bus\info.html')
