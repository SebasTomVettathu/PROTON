from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.

class tbl_chargingport(models.Model):
    port_name = models.CharField(max_length=100)
    port_details = models.CharField(max_length=50)
    watt = models.ForeignKey(tbl_watt, on_delete=models.CASCADE)
    port_amount = models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    cpo=models.ForeignKey(tbl_cpo,on_delete=models.CASCADE)
