from django.db import models

# Create your models here.

class Account(models.Model):
    ID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=50)
    fullName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phoneNumber = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class Activity(models.Model):
    ID = models.AutoField(primary_key=True)
    accountID = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='activity')
    visitHistory = models.JSONField(default = list,blank=True,max_length=5)
    
    def __str__(self):
        return self.visitHistory
    
    
class Business(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=100,null=True,blank=True)
    phoneNumber = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    ID = models.AutoField(primary_key=True)
    businessID = models.ForeignKey(Business,on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 100, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name


#Models for part 3:
class Order(models.Model):
    ID = models.AutoField(primary_key=True)
    businessID = models.ForeignKey(Business,on_delete=models.CASCADE)
    accountID = models.ForeignKey(Account,on_delete=models.CASCADE)
    products = models.JSONField(default=list)
    dateTime = models.DateTimeField(auto_now_add=True) #Extra added
    
    def __str__(self):
        return self.ID





    
    