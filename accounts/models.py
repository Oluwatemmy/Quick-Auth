from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from .manager import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    email = models.EmailField(unique=True, max_length=255, verbose_name= _("Email Address"))
    first_name = models.CharField(max_length=150, verbose_name=_("First name"))
    last_name = models.CharField(max_length=150, verbose_name=_("Last name"))

    is_staff = models.BooleanField(
        default=False
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(
        default=True
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(
        default=False
    )  # this field inherit from PermissionsMixin.
    is_verified = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    last_login = models.DateTimeField(
        auto_now=True
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        pass


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"{self.user.first_name} passcode"
