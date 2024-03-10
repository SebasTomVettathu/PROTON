from django.shortcuts import render
from CPO.models import *
# Create your views here.

def Homepage(request):
    cpo = tbl_cpo.objects.get(id=request.session["cid"])
    return render(request,"CPO/Homepage.html",{"cpo":cpo})

def myprofile(request):
    cpo = tbl_cpo.objects.get(id=request.session["cid"])
   
    return render(request,"CPO/Myprofile.html",{"cpo":cpo})

def Editprofile(request,id):
    Data=tbl_cpo.objects.get(id=cid)
    if request.method=="POST":
        Data.cpo_name=request.POST.get("txtname")
        Data.cpo_contact=request.POST.get("txtcontact")
        Data.cpo_email=request.POST.get("txtemail")
        Data.save()
        return redirect("webcpo:homepage") 
    else:
        return render(request, "CPO/Editprofile.html",{"Edit":Data})

def changepassword(request):
    cpo = tbl_cpo.objects.get(id=request.session["cid"])
    if request.method=="POST":
        if cpo.cpo_password==request.POST.get('txtcurrentpassword'):
            if request.POST.get('txtconfirmpassword')==request.POST.get('txtnewpassword'):
                cpo.cpo_password=request.POST.get('txtconfirmpassword')
        
                cpo.save()
                return render(request,"CPO/ChangePassword.html",{"cpo":cpo})
            else:
               return render(request,"CPO/ChangePassword.html",{"cpo":cpo})
        else: 
            return render(request,"CPO/ChangePassword.html",{"cpo":cpo})
    else:
        return render(request,"CPO/ChangePassword.html",{"cpo":cpo})


 

