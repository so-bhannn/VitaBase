import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email=self.normalize_email(email)
        user= self.model(email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault(is_staff=True)
        extra_fields.setdefault(is_superuser=True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=255)
    age=models.PositiveIntegerField()
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_doctor=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)

    unique_id=models.CharField(max_length=10, unique=True, editable=False)
    medical_record=models.TextField(blank=True, null=True)
    speciality= models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name', 'age', 'gender']

    objects=CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.unique_id:
            prefix='D-' if self.is_doctor else 'P-'
            self.unique_id=f'{prefix}{uuid.uuid4().hex[:8].upper()}'
        super().save(*args, **kwargs)
    
    def __str__(self):
        user_type='Doctor' if self.is_doctor else 'Patient'
        return f"{user_type} {self.email} {self.unique_id}"