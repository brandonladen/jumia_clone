from django.db import models

# Create your models here.
class Prod_Category(models.Model):
    Categ_Name = models.CharField(max_length=50)
    
class Product(models.Model):
    Category = models.ForeignKey('Prod_Category', on_delete=models.CASCADE)
    Prod_Name = models.CharField(max_length=50)
    Prod_Image = models.ImageField(upload_to = "path")
    Pod_Price = models.IntegerField()
    Pod_Description = models.TextField()
    
class Order(models.Model):
    Order_ID = models.CharField(max_length=50)
    Product_Name = models.ForeignKey('Product', on_delete=models.CASCADE)
    Date_Time = models.DateTimeField(auto_now_add=True)