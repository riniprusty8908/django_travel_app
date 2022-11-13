from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method =='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'UsernameTaken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'EmailTaken')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                print('user created')

        else:
            print("password not matching")
        return redirect('/')
    

    return render(request,'register.html')
