from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prod_Category(models.Model):
    Categ_Name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Categ_Name
    
class Product(models.Model):
    Category = models.ForeignKey('Prod_Category', on_delete=models.CASCADE)
    Prod_Name = models.CharField(max_length=50)
    Prod_Image = models.ImageField(upload_to = "static/assets/images")
    Pod_Price = models.IntegerField()
    Pod_Description = models.TextField()
    
    def __str__(self):
        return self.Prod_Name
    
    def display_img(self):
        return self.Prod_Image
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Order_ID = models.CharField(max_length=50)
    Product_ID = models.ForeignKey('Product', on_delete=models.CASCADE)
    Date_Time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Product_ID.Prod_Name