from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mob = models.CharField(verbose_name="Phone number", max_length=10, unique=True, validators=[validators.integer_validator, validators.MaxLengthValidator(10), validators.MinLengthValidator(10)])
    email = models.EmailField(verbose_name="Email", unique=True,validators=[validators.EmailValidator])
    firstName = models.CharField(verbose_name='First Name', max_length=250, validators=[validators.validate_slug])
    lastName = models.CharField(verbose_name='Last Name', max_length=250, validators=[validators.validate_slug])
    verified = models.BooleanField(default=False)
    code = models.CharField(default=None, max_length=10, null=True)
    def __str__(self):
        return str(self.firstName)+" "+str(self.lastName)
    

class Category(models.Model):
    product_category = models.CharField(verbose_name='Product Category', max_length=500, unique=True)
    def __str__(self):
        return str(self.product_category)


class SubCategory(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_subcategory = models.CharField(verbose_name='Product Sub Category', max_length=600, unique=True)
    def __str__(self):
        return str(self.product_subcategory)
    class Meta:
        order_with_respect_to = "product_category"

class Products(models.Model):
    product_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(verbose_name='Product Name', max_length=300)
    product_quantity = models.CharField(verbose_name='Product Quantity In Warehouse', max_length=100)
    product_description = models.CharField(verbose_name='Product Description', max_length=10000)
    product_price = models.CharField(verbose_name='Product Price', max_length=100)
    product_image = models.ImageField(verbose_name='Product Image')
    def __str__(self):
        return str(self.product_name)