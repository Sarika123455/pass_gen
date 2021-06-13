from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from user.forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User

# Create your views here.
# def userhome(request):
#     return render(request,'userhome.html')



     
# def userlogin(request):
#     if request.method =="POST":
#         form=AuthenticationForm(data=request.POST)  
#         if form.is_valid():
#             return redirect('userhome')
#     else:
#         form = AuthenticationForm()             
#     return render(request,'registration/login.html',{'form':form}) 

# def userlogin(request):
#     if request.method =="POST":
#         form=AuthenticationForm(data=request.POST)  
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username , password=password)
#         if user is not None:
#             if user.is_active:
#               login(request, user)
#             return redirect('userhome')
             
            
#     else:
#         form = AuthenticationForm() 
#         return render(request,'registration/login.html',{'form':form})       
   

