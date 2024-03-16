from django.shortcuts import render,redirect
from CPO.models import *
from Guest.models import *
from User.models import tbl_booking
# Create your views here.

def Homepage(request):
    cpo = tbl_cpo.objects.get(id=request.session["cid"])
    return render(request,"CPO/Homepage.html",{"cpo":cpo})

def myprofile(request):
    cpo = tbl_cpo.objects.get(id=request.session["cid"])
   
    return render(request,"CPO/Myprofile.html",{"cpo":cpo})

def Editprofile(request):
    Data=tbl_cpo.objects.get(id=request.session["cid"])
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


def chargingport(request):
    cpo = tbl_cpo.objects.get(id=request.session["cid"])
    district=tbl_district.objects.all()
    place1=tbl_place.objects.all()
    chargingport=tbl_chargingport.objects.filter(cpo=cpo)
    tdata=tbl_type.objects.all()
    if request.method == "POST": 
        place=tbl_place.objects.get(id=request.POST.get("place_id")) 
        watt=tbl_watt.objects.get(id=request.POST.get("watt_id"))
        tbl_chargingport.objects.create(
           port_name=request.POST.get("txtname"),
           port_details=request.POST.get("txtdetails"),
           watt=watt,
           port_amount=request.POST.get("txtamount"),
           place=place,
           cpo=cpo
            
        )
        
        return redirect("webcpo:chargingport")
    else:

        return render(request,"CPO/ChargingPort.html",{"data":chargingport,"place":place1,'type':tdata,'district':district})

def AjaxWatt(request):
    ttype=tbl_type.objects.get(id=request.GET.get("did"))
    watt=tbl_watt.objects.filter(type=ttype)
    return render(request,"CPO/AjaxWatt.html",{'watt':watt})

def DeletePort(request,id):
    tbl_chargingport.objects.get(id=id).delete()
    return redirect("webcpo:chargingport")

def ViewPortBooking(request):
    cpo = tbl_cpo.objects.get(id=request.session["cid"])
    data=tbl_booking.objects.filter(port__cpo=cpo)
    return render(request,"CPO/ViewPortBooking.html",{"data":data})

def Accept(request,id):
    booking=tbl_booking.objects.get(id=id)
    booking.booking_status=1
    booking.save()
    return redirect("webcpo:ViewPortBooking")

def Reject(request,id):
    booking=tbl_booking.objects.get(id=id)
    booking.booking_status=2
    booking.save()
    return redirect("webcpo:ViewPortBooking")

def logout(request):
    if 'cid' in request.session:
        del request.session['cid']
        return redirect('webguest:Login')
    else:
        return redirect('webguest:Login')                   