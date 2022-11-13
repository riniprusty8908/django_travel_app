from django.shortcuts import render,HttpResponse
from home.models import Contact, Destination
from django.contrib import messages



def index(request):
    dest=Destination.objects.all()

    return render(request,'index.html',{'dest':dest})



    
def about(request):
    return render(request,'about.html')
def link(request):
    return render(request,'link.html')
def trips(request):
    return render(request,'trips.html')
def stays(request):
    return render(request,'stays.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        EmailAddress=request.POST.get('EmailAddress')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,EmailAddress=EmailAddress,phone=phone,desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!!!')
    return render(request,'contact.html')
