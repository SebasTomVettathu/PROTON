from django.shortcuts import render
from Guest.models import *
# Create your views here.

def Homepage(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/Homepage.html",{"user":user})

def myprofile(request):
    user = tbl_user.objects.get(id=request.session["uid"])
   
    return render(request,"User/Myprofile.html",{"user":user})

def Editprofile(request,id):
    Data=tbl_user.objects.get(id=id)
    if request.method=="POST":
        Data.user_name=request.POST.get("txtname")
        Data.user_contact=request.POST.get("txtcontact")
        Data.user_email=request.POST.get("txtemail")

        Data.save()
        return redirect("webuser:homepage") 
    else:
        return render(request, "User/Editprofile.html",{"Edit":Data})

def changepassword(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        if user.user_password==request.POST.get('txtcurrentpassword'):
            if request.POST.get('txtconfirmpassword')==request.POST.get('txtnewpassword'):
                user.user_password=request.POST.get('txtconfirmpassword')
        
                user.save()
                return render(request,"User/ChangePassword.html",{"user":user})
            else:
               return render(request,"User/ChangePassword.html",{"user":user})
        else: 
            return render(request,"User/ChangePassword.html",{"user":user})
    else:
        return render(request,"User/ChangePassword.html",{"user":user})


 
