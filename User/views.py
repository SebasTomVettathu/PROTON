from django.shortcuts import render,redirect
from Guest.models import *
from CPO.models import  *
from User.models import *
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

 
def searchchargingport(request):
    district = tbl_district.objects.all()
    place = tbl_place.objects.all()
    ttype = tbl_type.objects.all()
    data=tbl_chargingport.objects.all()
    
    return render(request,"User/SearchChargingPort.html",{"data":data,"district":district,"place":place,"type":ttype})

def AjaxPort(request):
    if request.GET.get("did") != "" and request.GET.get("pid")!="" and request.GET.get("tid")!="":
        district=tbl_district.objects.get(id=request.GET.get("did"))
        place=tbl_place.objects.get(id=request.GET.get("pid"))
        type=tbl_type.objects.get(id=request.GET.get("tid"))
        data=tbl_chargingport.objects.filter(place=place,place__district=district,watt__type=type)
        return render(request,"User/AjaxPort.html",{"data":data})
    elif request.GET.get("did") != "" and request.GET.get("pid")!="" :
        district=tbl_district.objects.get(id=request.GET.get("did"))
        place=tbl_place.objects.get(id=request.GET.get("pid"))
        data=tbl_chargingport.objects.filter(place=place,place__district=district)
        return render(request,"User/AjaxPort.html",{"data":data})
    elif request.GET.get("did") != ""  and request.GET.get("tid")!="":
        district=tbl_district.objects.get(id=request.GET.get("did"))
        type=tbl_type.objects.get(id=request.GET.get("tid"))
        data=tbl_chargingport.objects.filter(place__district=district,watt__type=type)
        return render(request,"User/AjaxPort.html",{"data":data})
    elif  request.GET.get("pid")!="" and request.GET.get("tid")!="":
        place=tbl_place.objects.get(id=request.GET.get("pid"))
        type=tbl_type.objects.get(id=request.GET.get("tid"))
        data=tbl_chargingport.objects.filter(place=place,watt__type=type)
        return render(request,"User/AjaxPort.html",{"data":data})
    elif request.GET.get("did") != "" :
        district=tbl_district.objects.get(id=request.GET.get("did"))
        data=tbl_chargingport.objects.filter(place__district=district)
        return render(request,"User/AjaxPort.html",{"data":data})
    elif request.GET.get("pid")!="" :
        place=tbl_place.objects.get(id=request.GET.get("pid"))
        data=tbl_chargingport.objects.filter(place=place)
        return render(request,"User/AjaxPort.html",{"data":data})
    elif  request.GET.get("tid")!="":
        type=tbl_type.objects.get(id=request.GET.get("tid"))
        data=tbl_chargingport.objects.filter(watt__type=type)
        return render(request,"User/AjaxPort.html",{"data":data})
    else:
        data=tbl_chargingport.objects.all()
        return render(request,"User/AjaxPort.html",{"data":data})
    
def PortBooking(request,id):
    user=tbl_user.objects.get(id=request.session["uid"])
    port=tbl_chargingport.objects.get(id=id)
    amnt=port.port_amount
    if request.method=="POST":
        tbl_booking.objects.create(port=port,user=user,booking_amount=amnt,
                                   booking_fordate=request.POST.get('date'),booking_fortime=request.POST.get('time'))
        return redirect('webuser:homepage')
    else:
        return render(request,"User/PortBooking.html",{'amnt':amnt})
    
def ViewPortBooking(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_booking.objects.filter(user=user)
    return render(request,"User/ViewPortBooking.html",{"data":data})

def Payment(request,id):
    booking=tbl_booking.objects.get(id=id)
    amnt=booking.booking_amount
    if request.method=="POST":
        booking.booking_status=3
        booking.save()
        return redirect("webuser:ViewPortBooking")
    else:
        return render(request,"User/Payment.html",{"amnt":amnt})
    
def Complaint(request):
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    Complaint=tbl_complaint.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_complaint.objects.create(user=customerdata,
                                    complaint_title=request.POST.get("txttit"),
                                    complaint_content=request.POST.get("txtcomplaint"))
       return redirect("webuser:Complaint")
    else:
        return render(request,"User/Complaint.html",{'complaint':Complaint}) 

def Delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("webuser:Complaint")

def Feedback(request):
    customerdata=tbl_user.objects.get(id=request.session["uid"])
    feedback=tbl_feedback.objects.filter(user=customerdata)
    if request.method=="POST":
       tbl_feedback.objects.create(user=customerdata,
                                   feedback_content=request.POST.get("txtpro"))
       return redirect("webuser:Feedback")
    else:
        return render(request,"User/Feedback.html",{'feedback':feedback})       

def Delfeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("webuser:Feedback")   

def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('webguest:LoadMainIndex')
    else:
        return redirect('webguest:LoadMainIndex')       