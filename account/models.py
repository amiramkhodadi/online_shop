from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from datetime import timedelta
import random


class MyUserManager(BaseUserManager):
    def create_user(self, phone=None ,full_name=None, password=None):
        if not phone:
            raise ValueError("Users must have an phone number")

        user = self.model(
            phone=phone
,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, full_name,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,full_name,
            password=password,


        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(
        verbose_name="phone number",
        max_length=12,
        unique=True,
        null=True,
        blank=True,
    )
    full_name = models.CharField(verbose_name="full name", max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(blank = True, max_length=255 , unique=True , null=True )
    objects = MyUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class VerificationCode(models.Model):
    phone = models.CharField(verbose_name="phone number", max_length=12)
    code = models.CharField(max_length=6)
    expires_at = models.DateTimeField()

    def is_valid(self):
        return timezone.now() <= self.expires_at

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - Valid: {self.is_valid()} - {self.phone}"