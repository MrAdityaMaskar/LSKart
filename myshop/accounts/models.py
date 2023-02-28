from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


class UserType(models.Model):
    BUYER = 1
    SELLER = 2
    TYPE_CHOICES = (
        (SELLER, 'Seller'),
        (BUYER, 'Buyer')

    )
    id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES,primary_key=True)
    
    def __str__(self) -> str:
        return self.get_id_display()
    
    
    

class User(AbstractUser, PermissionsMixin):
    
    date_joined = models.DateTimeField(default= timezone.now)
    usertype = models.ManyToManyField(UserType)
    username= models.CharField(_("Username"), max_length=50,primary_key=True)
    email = models.EmailField(_('email address main'), unique=True)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=10)
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS= ['username','first_name','last_name', 'phone','address']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    

    