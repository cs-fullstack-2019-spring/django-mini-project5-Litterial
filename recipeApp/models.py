from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NewUser(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    picture=models.CharField(max_length=200)
    userTableForeignKey=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.username


class RecipieInfo(models.Model):
    picture=models.CharField(max_length=200)
    meal_name=models.CharField(max_length=200)
    description=models.TextField()
    ingredients=models.TextField()
    directions=models.TextField()
    date_created=models.DateField()
    creator=models.CharField(max_length=200)
    keytoNewUser=models.ForeignKey(NewUser,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.meal_name