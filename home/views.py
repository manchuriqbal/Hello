from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        "variable": "contact with me for this type of website"
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def service(request):
     return render(request, "service.html")


def contact(request):
     if request.method == "POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            decs=request.POST.get('decs')
            contact=Contact(name=name, email=email, mobile=mobile, decs=decs, date=datetime.today())
            contact.save()
            messages.success(request, 'Your message successfully send!')
     return render(request, "contact.html")
