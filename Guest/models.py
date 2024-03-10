from django.db import models
from Admin.models import *

# Create your models here.


    
    
    
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_type=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='Assets/UserPhoto/')
    user_proof=models.FileField(upload_to='Assets/UserProof/')
    place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)

class tbl_cpo(models.Model):
    cpo_id = models.CharField(max_length=100)
    cpo_name = models.CharField(max_length=100)
    cpo_contact=models.CharField(max_length=50)
    cpo_email = models.EmailField(max_length=50)
    cpo_password = models.CharField(max_length=50)
    station_name = models.CharField(max_length=50)
    station_proof = models.FileField(upload_to='Assets/CpoProof/')
    place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)


