from django.shortcuts import render, HttpResponse

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
     return render(request, "contact.html")
