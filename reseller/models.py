from django.db import models

# Create your models here.

class Reseller(models.Model):
    s_name = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    upload_image = models.ImageField(upload_to = 'reseller/')
    password = models.CharField(max_length=20)
