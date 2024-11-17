from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.core.validators import MaxValueValidator,MinValueValidator
class Category(models.Model):
    category_name=models.CharField(max_length=120,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name=models.CharField(max_length=120,unique=True)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=120)

    def __str__(self):
        return self.product_name

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")

    )
    status=models.CharField(max_length=120,choices=options,default="in-cart")

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together=("user","product")

