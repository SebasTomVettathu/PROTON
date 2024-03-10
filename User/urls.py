from django.urls import path
from User import views
app_name="webuser"
urlpatterns=[
    path('Homepage' ,views.Homepage,name="homepage"),
   
    path('myprofile' ,views.myprofile,name="myprofile"),
    
    path('changepassword',views.changepassword,name="changepassword"),
    path('editprofile/<int:id>',views.Editprofile,name="editprofile"),

    path('myprofile' ,views.myprofile,name="myprofile"),
]