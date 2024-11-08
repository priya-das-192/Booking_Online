from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,template_name='bus\home.html')

def seat (request):
    return render(request,template_name='bus\seat.html')
def ticket_info (request):
    return render(request,template_name='bus\ticket_info.html')