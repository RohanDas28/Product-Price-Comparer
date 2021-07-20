from django.shortcuts import render
from .models import Contact

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        # print(request)
        email = request.POST.get("email")
        name= request.POST.get("name")
        phone= request.POST.get("number")
        desc = request.POST.get("desc")
        cnt = Contact(email=email,name=name,phone=phone,desc=desc)
        # print(cnt)
        cnt.save()
    return render(request, 'contact.html')


def results(request):
    return render(request, 'results.html')


def services(request):
    return render(request, 'services.html')
