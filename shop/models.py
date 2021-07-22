from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date =models.DateField()
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name



class Contact(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name= models.CharField(max_length=70)
    email= models.CharField(max_length=70)
    address= models.CharField(max_length=700)
    city= models.CharField(max_length=70)
    state= models.CharField(max_length=70)
    zip_code= models.CharField(max_length=70)
    phone= models.CharField(max_length=70,default="")

    def __str__(self):
        return self.name


