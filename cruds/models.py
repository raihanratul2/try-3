from django.db import models
from datetime import date

# Create your models here.


class profile(models.Model):
    RELIGION = (
        ('one','Muslim'),
        ('two','Hindu',),
        ('three','Christian',),
        ('four','Bouddho',),
        ('five','others',),
    )
    GENDER = (
        ('one','Male'),
        ('two','Female'),
        ('three','others'),
    )
    name = models.CharField(max_length=20, blank=True,null=True)
    email = models.EmailField(max_length=30, blank=True,null=True)
    age = models.PositiveBigIntegerField()
    adress = models.TextField(max_length=200)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(("Date"), auto_now_add=True)
    gender = models.CharField(max_length=8, choices=GENDER, blank=True, null=True)
    religion = models.CharField(max_length=10, choices=RELIGION, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pic/')
    
    print(image,religion,gender,date_of_birth,phone,adress,age,email,name)


    def __str__(self): 
        return str(self.name)
    
