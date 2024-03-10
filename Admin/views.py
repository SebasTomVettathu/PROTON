from django.shortcuts import render,redirect
from Admin.models import *

def district(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get('txtdis'))
        return render(request,"Admin/District.html",{"data":district})
    else:
        return render(request,"Admin/District.html",{"data":district})

  # Make sure to import your model

def adminReg(request):
    admin=tbl_admin.objects.all()
    if request.method == "POST":
        tbl_admin.objects.create(
            admin_name=request.POST.get("txtname"),
            admin_contact=request.POST.get("txtcontact"),
            admin_email=request.POST.get("txtemail"),
            admin_password=request.POST.get("txtpassword"),
        )
        return render(request, "Admin/AdminReg.html",{"data":admin})
    else:
        return render(request, "Admin/AdminReg.html",{"data":admin})

def adminDelete(request,id):
  tbl_admin.objects.get(id=id).delete()
  return redirect('webadmin:Admin')


def districtDelete(request,id):
  tbl_district.objects.get(pk=id).delete()
  return redirect("webadmin:District")

def editadminReg(request,id):
    Data=tbl_admin.objects.get(id=id)
    if request.method=="POST":
        Data.admin_name=request.POST.get('txtname')
        Data.admin_contact=request.POST.get('txtcontact')
        Data.admin_email=request.POST.get('txtemail')
        Data.admin_password=request.POST.get('txtpassword')
        Data.save()
        return redirect("webadmin:Admin")

    else:
     return render(request, "Admin/AdminReg.html",{"Edit":Data})

def editDistrict(request,id):
    Data=tbl_district.objects.get(id=id)
    if request.method == "POST":
        Data.district_name = request.POST.get('txtdis')
        Data.save()
        return redirect("webadmin:District")
        
    else:
      return render(request, "Admin/District.html",{"Edit":Data})

def place(request):
    dis=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        dist=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(
           place_name=request.POST.get("txtname"),
           district = dist
        )
        return render(request,"Admin/Place.html",{"data":place})
    else:
        return render(request,"Admin/Place.html",{"data":place,"district":dis})

def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return render(request,"Admin/Place.html",{'data':data})
    else:
        return render(request,"Admin/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("webadmin:Place")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    data=tbl_place.objects.all()
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("webadmin:Place")
    else:
        return render(request,"Admin/Place.html",{"editdata":editdata,"district":district,"data":data})

def Homepage(request):
     admin = tbl_admin.objects.get(id=request.session["aid"]),
     return render(request,"Admin\Homepage.html")
   
