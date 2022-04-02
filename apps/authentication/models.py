from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, Balance, password=None):
        if not email:
            raise ValueError("users must have an email adresse")
        if not username:
            raise ValueError("users must have an username")
        if not Balance:
            raise ValueError("users must have Balance")

        user = self.model(
            email=self.normalize_email(email),
            username= username,
            Balance = Balance,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, Balance, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            Balance= Balance,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
 	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(verbose_name="username", max_length=30, unique=True)
    Balance = models.CharField(verbose_name="Balance", max_length=20, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["Balance", "username"]

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Meta:
        app_label = 'apps_auth'


