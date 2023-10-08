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
    
