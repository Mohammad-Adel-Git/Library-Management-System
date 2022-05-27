# from typing_extensions import Required
from django.db import models
# Create your models here.
class addBook(models.Model):
    category=models.CharField(max_length=250)
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    publication_year=models.IntegerField()
    ISBN=models.CharField(max_length=250)
    def __str__(self):
        return self.title
    
class Loginadmin(models.Model):
    Email=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.Email
    

class SignUpAdmin(models.Model):
    firsTName=models.CharField(max_length=250)
    lastName=models.CharField(max_length=250)
    Email=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    confirm_password=models.CharField(max_length=250)
    def __str__(self):
        return self.Email       

class User(models.Model):
    name = models.CharField(max_length=20)
    familyName = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=100)


class SignUpUser(models.Model):
    firstName=models.CharField(max_length=250)
    lastName=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    confirm_password=models.CharField(max_length=250)
    def __str__(self):
        return self.email     

class addBooks(models.Model):
    category=models.CharField(max_length=250)
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    publication_year=models.IntegerField()
    ISBN=models.CharField(max_length=250)
    def __str__(self):
        return self.title