from django.urls import path
from CPO import views
app_name="webcpo"
urlpatterns=[
    path('Homepage' ,views.Homepage,name="homepage"),
   
    path('myprofile' ,views.myprofile,name="myprofile"),
    
    path('changepassword',views.changepassword,name="changepassword"),
    path('editprofile/',views.Editprofile,name="editprofile"),


    path('chargingport/',views.chargingport,name="chargingport"),

    path('AjaxWatt/',views.AjaxWatt,name="AjaxWatt"),

    path('DeletePort/<int:id>',views.DeletePort,name="DeletePort"),

    path('ViewPortBooking' ,views.ViewPortBooking,name="ViewPortBooking"),

    path('Accept/<int:id>',views.Accept,name="Accept"),

    path('Reject/<int:id>',views.Reject,name="Reject"),
    
    path("logout/",views. logout,name="logout"),
]