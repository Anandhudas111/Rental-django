from django.db import models
from django.contrib.auth.models import User


# Create your models here. 
class Contact(models.Model):
    email=models.EmailField()
    message=models.TextField()

class vendor(models.Model):
   
    username=models.CharField(max_length=255)
    userid=models.IntegerField()
    password=models.CharField(max_length=255)
    

    
class Category(models.Model):
    
    title=models.CharField(max_length=50,verbose_name="product_title")
    slug=models.SlugField(max_length=55,verbose_name="category_slug")
    description=models.TextField(blank=True,verbose_name='category_description')
    category_image=models.ImageField(upload_to='media/category',blank=True,null=True,verbose_name='category_image')
    is_active=models.BooleanField(verbose_name="is_active")
    is_featured=models.BooleanField(verbose_name="is_featured")

    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        return self.title
    
class Product(models.Model):
    STATUS_CHOICES=[
        ('available','available'),
        ('non_available','non_available'),
    ]

    title=models.CharField(max_length=150,verbose_name="Product title")
    slug=models.SlugField(max_length=160,verbose_name="Product slug")
    sku=models.CharField(max_length=255,unique=True,verbose_name="Product ID ")
    detail_description = models.TextField(blank=True, null=True, verbose_name="Detail Description")
    product_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name="Product Image")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="Product Categoy", on_delete=models.CASCADE)
    is_present = models.BooleanField(verbose_name="Is present",null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    status=models.CharField(choices=STATUS_CHOICES,max_length=100,default="available")
    

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title
    
class Relatedimage(models.Model):
    products=models.ForeignKey(Product,default=None,on_delete=models.CASCADE)
    image=models.FileField(upload_to='relate',null=True)

class Wishlist(models.Model):
    title=models.CharField(max_length=120,verbose_name='wish title')
    user=models.ForeignKey(User,verbose_name="user",on_delete=models.CASCADE)
    product=models.ForeignKey(Product,verbose_name='Product',null=True, on_delete=models.CASCADE)
    slug=models.CharField(max_length=30,null=True,blank=True)
    added_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
   

class Booking(models.Model):
   
 
    user=models.ForeignKey(User,verbose_name='user',null=True,on_delete=models.CASCADE)
    sku=models.CharField(max_length=255,unique=True,default="",verbose_name="Product ID ")
    phonenumber=models.CharField(max_length=10,default="")
    streetaddress=models.CharField(max_length=10,default="")
    address=models.CharField(max_length=10,default="")
    pincode=models.CharField(max_length=10,default="")
    country=models.CharField(blank=True,default="india",verbose_name='country',max_length=10)
    product=models.ForeignKey(Product,verbose_name='product',default=None,on_delete=models.CASCADE)
    price=models.IntegerField()
