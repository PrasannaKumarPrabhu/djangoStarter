from django.shortcuts import render, HttpResponse
from datetime import date
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'variable': "Prasanna"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is my homePage")


def about(request):
    return render(request, 'about.html')


# return HttpResponse("this is my about us")


def services(request):
    return render(request, 'index.html')


# return HttpResponse("this is my services")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact_var = Contact(name=name, email=email, phone=phone, desc=desc, date=date.today())
        contact_var.save()
        messages.success(request,"Your contact request has been sent")
    return render(request, 'contact.html')
# return HttpResponse("this is my contact us")
