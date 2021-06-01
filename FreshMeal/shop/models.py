from django.db import models

# Create your SHOP models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images",default="") 
    
    def __str__(self):
	    return (self.product_name)
        
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=70, default="")
    
    def __str__(self):
        return self.email

class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    pincode=models.CharField(max_length=111)
        
