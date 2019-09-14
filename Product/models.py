from django.db import models


class menubar(models.Model):
   name = models.CharField(max_length=50)
   sub_menu = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

   def __str__(self):
       return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    delivery = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.name


class Product_image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.product.name


class Product_feature(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.TextField(blank=True)

    def __str__(self):
        return self.product.name
