from django.db import models

# Create your models here.

class Product(models.Model):
    categories = (('Mens','Mens'),('Womens','Womens'),('Kids','Kids'),('Mens Sneakers','Mens Sneakers'),('Womens Sneakers','Womens Sneakers'))
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='images',default='')
    product_category = models.CharField(max_length=50,choices=categories,default='')

    def __str__(self):
        return str(self.product_name)
