from django.urls import path
from User import views
app_name="webuser"
urlpatterns=[
    path('Homepage' ,views.Homepage,name="homepage"),
   
    path('myprofile' ,views.myprofile,name="myprofile"),
    
    path('changepassword',views.changepassword,name="changepassword"),
    path('editprofile/<int:id>',views.Editprofile,name="editprofile"),

    path('myprofile' ,views.myprofile,name="myprofile"),

    path('SearchChargingPort' ,views.searchchargingport,name="searchchargingport"),

    path('AjaxPort' ,views.AjaxPort,name="AjaxPort"),

    path('PortBooking/<int:id>' ,views.PortBooking,name="PortBooking"),

    path('ViewPortBooking' ,views.ViewPortBooking,name="ViewPortBooking"),

    path('Payment/<int:id>' ,views.Payment,name="Payment"),

    path("Complaint/",views.Complaint,name="Complaint"),
    path("Delcomplaint/<int:did>", views.Delcomplaint,name="Delcomplaint"),
    path("Feedback/",views.Feedback,name="Feedback"),
    path("Delfeedback/<int:did>", views.Delfeedback,name="Delfeedback"),

    path("logout/",views. logout,name="logout"),
]