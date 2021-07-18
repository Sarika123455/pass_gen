from django.contrib.auth import forms
from django.shortcuts import redirect, render,redirect
from django.contrib.auth.forms import AuthenticationForm
from multiselectfield.db.fields import MultiSelectField
from admin_app.models import  Loan, Member,Societyloan
from admin_app.forms import Memberform,SocietyForm,LoanForm
from admin_app.forms import SignupForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import Settings, settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as Login_process
from django.db.models import Q

# Create your views here.



@login_required
def home(request):
    return render(request,'home.html')

@login_required
def userhome(request):
    return render(request,'userhome.html')


@login_required
def Signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addmember')
          
    else:
        form=SignupForm()
    return render(request,'registration.html',{'form':form})  

def login(request):
    if request.method =="POST":
        form=AuthenticationForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user and user.is_staff is False:
            Login_process(request, user)
            return redirect('userhome')
        elif user and user.is_staff is True:
            Login_process(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()             
    return render(request,'registration/login.html',{'form':form})     


@login_required
def addmember(request):
    if request.method == "POST":
        
        form=Memberform(request.POST,request.FILES)
        if form.is_valid():
            messages.success(request, 'Add Member Successfully..')
            form.save()
            
    else:
        form=Memberform()
    return render(request,'addmember.html',{'form':form,})    

@login_required
def societyloan(request):
    if request.method == "POST":
        form=SocietyForm(request.POST,request.FILES)
        if form.is_valid():
            messages.success(request, 'Save Successfully..')
            form.save()
            return redirect('societyloanread')
            
         
    else:
      
       form = SocietyForm()  
    return render(request,'societyloan.html',{'form':form})      
            
    
     
@login_required   
def allloan(request):
    mobiles = Member.objects.all()
    return render(request,'rdmember.html' ,{'mobiles':mobiles})  
  
    
@login_required
def memberread(request):
    read=Member.objects.filter(user=request.user)
    return render(request,'memberdetails.html',{'read':read})  


  
    

def search(request):
     query = request.GET['query']
     mobiles = Member.objects.filter(full_name__icontains=query)
     search = {'mobiles':mobiles}
    # if request.method == 'GET':
    #     search = request.GET.get('search')    
    #     post = Member.objects.all().filter(full_name=search)
     return render(request, 'rdmember.html',{'mobiles':mobiles})



@login_required            
def societyloanread(request):
    read=Societyloan.objects.all()
    return render(request,'societyloanread.html',{'read':read})  

@login_required
def memberloan(request):
    read=Loan.objects.filter(user=request.user) 
    return render(request,'memberloanread.html',{'read':read})  

@login_required
def memberloanform(request):
    if request.method == "POST":
        
        form=LoanForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            messages.success(request, 'Save Successfully..')
            form.save()
            return redirect(memberloanread)

            
    else:
        form=LoanForm()
    return render(request,'memberloanform.html',{'form':form,})        

@login_required
def memberloanread(request):
    read=Loan.objects.all()
    return render(request,'loanreadmember.html',{'read':read})  

def loanupdate(request,id):
    upd=Loan.objects.get(id=id)
    fm=LoanForm(request.POST or None,request.FILES or None,instance=upd)
    if fm.is_valid():
        fm.save()
        return redirect(memberloanread)
    return render(request,'loanupdate.html',{'update':fm})   

@login_required
def loandelete(request,id):
    dele=Loan.objects.get(id=id)
    dele.delete()
    return redirect(memberloanread)  

@login_required
def memberupdate(request,id):
    upd=Member.objects.get(id=id)
    fm=Memberform(request.POST or None,request.FILES or None,instance=upd)
    if fm.is_valid():
        fm.save()
        return redirect(allloan)
    return render(request,'memberupdate.html',{'update':fm})   


@login_required
def memberdelete(request,id):
    dele=Member.objects.get(id=id)
    dele.delete()
    return redirect(allloan) 

@login_required
def societyupdate(request,id):
    upd=Societyloan.objects.get(id=id)
    fm=SocietyForm(request.POST or None,request.FILES or None,instance=upd)
    if fm.is_valid():
        fm.save()
        return redirect(societyloanread)
    return render(request,'societyupdate.html',{'update':fm})   


@login_required
def societydelete(request,id):
    dele=Societyloan.objects.get(id=id)
    dele.delete()
    return redirect(societyloanread)         

@login_required
def loansocietyread(request):
    read=Societyloan.objects.filter(user=request.user) 
    return render(request,'loansocietyread.html',{'read':read})


def societysearchloan(request):
    # query = request.GET['query']
    # read = Loan.objects.filter(status__icontains=query)
    # search = {'read':read}
    if request.method == 'GET':
        search = request.GET.get('query')
        # read = Loan.objects.all().filter(status=search)
        read =[item for item in Loan.objects.all() if search in item.status ]
    return render(request, 'loanreadmember.html',{'read':read})

@login_required
def monthsearchloan(request):
    if request.method == 'POST':
        fd=request.POST.get('startmonth')
        to=request.POST.get('endmonth')
        name=request.POST.get('name')
        searchresult=Loan.objects.filter(Q(month__gte=fd) & Q(month__lte=to) & Q(full_name=name))
        d = {'read':searchresult,'fd':fd,'to':to,'name':name}
        return render(request,'loanreadmember.html',d)
    return render(request, 'loanreadmember.html')        


# def societysearchloans(request):
#     if request.method == 'GET':
#         search = request.GET.get('name')
#         read = Loan.objects.all().filter(Loan__user=search)
#         # read =[item for item in User.objects.all() if search in item.User ]
#     return render(request, 'loanreadmember.html',{'read':read})
    
       

#     query = request.GET['query']
#     read = Societyloan.objects.filter(full_name__exact=query)
#     search = {'read':read}
#     # if request.method == 'GET':
#     #     search = request.GET.get('query')    
#     #     read = Loan.objects.all().filter(full_name=search)
#     return render(request, 'societyloanread.html',{'read':read})