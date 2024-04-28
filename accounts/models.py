from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Enquiries(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    services = models.CharField(max_length=255)
    date_enquired = models.DateField()
    status = models.CharField(max_length=255)

