from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        "variable": "contact with me for this type of website"
    }
    return render(request, "index.html", context)


def about(request):
    return HttpResponse("this is about pages")


def service(request):
    return HttpResponse("this is service pages")


def contact(request):
    return HttpResponse("this is contact pages")
