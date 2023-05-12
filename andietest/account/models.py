from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    def __str__(self):
      return self.username

class Activity(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    page_visits = models.JSONField()
    
class Business(models.Model):
    business_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    def __str__(self):
      return self.business_name
    
class Item(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1, blank=True)
    def __str__(self):
       return self.item_name