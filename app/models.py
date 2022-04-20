from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from config import settings
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Institution(models.Model):

    INSTITUTION_TYPE = [
        ("foundation", "fundacja"),
        ("order_organization", "organizacja porządkowa"),
        ("local_collection", "zbiórka lokalna")
    ]

    name = models.CharField(max_length=250)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=INSTITUTION_TYPE, default="foundation")
    categories = models.ManyToManyField(Category, related_name="institutions")

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()

    phoneNumber = PhoneNumberField(unique=True, null=False, blank=False)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=6)

    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(blank=True)

    categories = models.ManyToManyField(Category, related_name="categories")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="institution")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="user", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pick_up_date}"


