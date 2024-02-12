from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise  ValueError("Username can't be empty")
        

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
            )
        
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


# Create your models here.
class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone  = models.CharField(max_length=30)

    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
