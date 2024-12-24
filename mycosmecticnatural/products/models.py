from django.db import models

# Create your models here.
'''
    Each product should have the following attributes: Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date.
Ensure validation for required fields like Price, Name, and Stock Quantity.
Make sure the Stock Quantity is automatically reduced when an order is placed (future enhancement or consider as optional for now).
'''

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='products/', blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name