from django.shortcuts import render,redirect
from Admin.models import  *
from Guest.models import  *


def Homepage(request):
    return render(request, "Guest/Homepage.html") 

def Login(request):
    if request.method == "POST":
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txtemail"),admin_password=request.POST.get("txtpassword")).count()
        usercount=tbl_user.objects.filter(user_email=request.POST.get("txtemail"),user_password=request.POST.get("txtpassword")).count()

        if admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txtemail"),admin_password=request.POST.get("txtpassword"))
            request.session["aid"] = admin.id
            return redirect("webadmin:homepage")
        elif(usercount > 0):
            user=tbl_user.objects.get(user_email=request.POST.get("txtemail"),user_password=request.POST.get("txtpassword"))
            request.session["uid"] = user.id
            return redirect("webuser:homepage")
        
        else:
            return render(request,"Guest/Login.html")
    else:   
        return render(request,"Guest/Login.html")

def newuser(request):
    place1=tbl_place.objects.all()
    user=tbl_user.objects.all()
    if request.method == "POST": 
        place=tbl_place.objects.get(id=request.POST.get("place_id")) 
        tbl_user.objects.create(
            user_name=request.POST.get("txtname"),
            user_gender=request.POST.get("txtgender"),
            user_contact=request.POST.get("txtcontact"),
            user_email=request.POST.get("txtemail"),
            user_password=request.POST.get("txtpaswd"),
            user_type=request.POST.get("txttype"),
            user_photo=request.FILES.get("fileimg"),
            user_proof=request.FILES.get("fileimgproof"),
            place=place
            
        )
        
        return redirect("webguest:Newuser")
    else:

        return render(request,"Guest/Newuser.html",{"data":user,"place":place1})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/ajaxPlace.html",{"placedata":place} )

def cporegistration(request):
    place1=tbl_place.objects.all()
    cpo=tbl_cpo.objects.all()
    if request.method == "POST": 
        place=tbl_place.objects.get(id=request.POST.get("place_id")) 
        tbl_cpo.objects.create(
            cpo_name=request.POST.get("txtname"),
            cpo_contact=request.POST.get("txtcontact"),
            cpo_email=request.POST.get("txtemail"),
            cpo_password=request.POST.get("txtpaswd"),
            station_name=request.POST.get("txtname"),
            station_proof=request.FILES.get("fileimgproof"),
            place=place
            
        )
        
        return redirect("webguest:Cporegistration")
    else:

        return render(request,"Guest/Cporegistration.html",{"data":cpo,"place":place1})
