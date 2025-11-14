from django.db import models

class User(models.Model):
    username=models.CharField(max_length=250,unique=True,default="Enter your username")
    email=models.EmailField(max_length=450,unique=True)
    age=models.IntegerField(
                            choices=[
                                ("Minor","Below 18"),
                                ("ADULT","18 +"),
                                ("SENIOUR"," 65 +")
                            ])

# Create your models here.
    #def __str__(self):

