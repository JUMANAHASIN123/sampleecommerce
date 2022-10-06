from django.shortcuts import render

# Create your views here.

def customer_views(request):
    return render(request,'customer/customerview.html')