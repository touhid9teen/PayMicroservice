from django.db import models
from django.contrib.auth.models  import BaseUserManager,AbstractUser

class AuthUserManagement(BaseUserManager):
    def create(self,username,email, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is not found !')
        if not email:
            raise ValueError('Email is not found !')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, password):
        user = self.create(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AuthUser(AbstractUser):
    username = models.CharField(max_length=100,unique=True, null=True,blank=True)
    email = models.EmailField(max_length=100, unique=True)
    user_number = models.CharField(max_length=11,unique=True)
    current_balance = models.DecimalField(max_digits=12,decimal_places=2)
    password = models.CharField(max_length=100)

    objects = AuthUserManagement()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']





