from django.db import models

# Create your models here.
class Prod_Category(models.Model):
    Categ_Name = models.CharField(max_length=50)
    
class Poduct(models.Model):
    Category = models.ForeignKey('Prod_Category', on_delete=models.CASCADE)
    Prod_Name = models.CharField(max_length=50)
    Prod_Image = models.ImageField(upload_to = "path")
    Prod_Image_Desc = models.ImageField(upload_to = "path", null=True, blank=True)
    Pod_Price = models.IntegerField()
    Pod_Description = models.TextField()