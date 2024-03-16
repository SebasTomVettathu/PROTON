from django.urls import path
from Guest import views
app_name="webguest"


urlpatterns = [
    path('Homepage/',views.Homepage,name="Homepage"),

    path('Newuser/',views.newuser,name="Newuser"),

    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),

    path('Login/',views.Login,name="Login"),
    
    path('Cporegistration/',views.cporegistration,name="Cporegistration"),
    
   
]