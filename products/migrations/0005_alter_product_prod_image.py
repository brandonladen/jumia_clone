# Generated by Django 5.0.1 on 2024-02-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_prod_image_desc_alter_order_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Prod_Image',
            field=models.ImageField(upload_to='static/assets/images'),
        ),
    ]