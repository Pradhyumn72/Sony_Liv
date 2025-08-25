from django.shortcuts import render
from .models import User
from django.http import HttpResponse

# Create your views here.
def Landing(req):
    return render(req,'Landing.html')
def  Shows(req):
    return render(req,'Shows.html')
def  Movies(req):
    return render(req,'Movies.html')
def Sports(req):
    return render(req,'Sports.html')
def Premium(req):
    return render(req,'Premium.html')


    
def Signup(req):
    if req.method=="POST":
        n=req.POST.get('name')
        e=req.POST.get('email')
        p=req.POST.get('password')
        cp=req.POST.get('cpass')
        data=User.objects.filter(email=e)
        if data:
            errem="email already exists"
            return render(req,'Signup.html',{'errem':errem,'Signup':'Signup'})
        else:
            if p==cp:
                User.objects.create(Name=n,Email=e,Password=p)
                msg="Registration Done"
                return render(req,'Landing.html',{'Login':'Login'})
            else:
                msg="Password and Confirm Password not matched "
    return render(req,'Signup.html')

def Login(req):
    if req.method=="POST":
        e=req.POST.get('email')
        p=req.POST.get('password')
        data=User.objects.filter(Email=e)
        if data:
           
           userr=User.objects.get(Email=e)
           passs=userr.Password
           if passs==p:
               data={'Name':userr.Name,'Email':userr.Email,'Password':userr.Password}
               return render(req,'Landing.html',{'data':data})
           else:
               err="Crendtials do not match"
               return render(req,'Signup.html',{'err':err})
        else:
           emr="Email does not exist"
           return render(req,'Signup.html',{'emr':emr})
    else:
        return render(req,'Signup.html')  