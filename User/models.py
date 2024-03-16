from django.db import models

from CPO.models import tbl_chargingport
from Guest.models import tbl_user

# Create your models here.

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_fordate=models.DateField()
    booking_fortime=models.TimeField()
    port=models.ForeignKey(tbl_chargingport,on_delete=models.CASCADE)
    booking_amount=models.CharField(max_length=10)
    booking_status=models.CharField(max_length=20,default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    complaint_status=models.CharField(default=0,max_length=10)
    complaint_title=models.CharField(max_length=100)
    complaint_content=models.CharField(max_length=300)
    complaint_reply=models.CharField(default='Not replied',max_length=100)
    complaint_date=models.DateField(auto_now_add=True)

class tbl_feedback(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    feedback_content=models.CharField(max_length=300)
    feedback_date=models.DateField(auto_now_add=True)


    