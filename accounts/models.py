from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
import uuid
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
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['name', 'age', 'gender']

    objects=CustomUserManager()
    
    def __str__(self):
        return self.email
    
class Patient(CustomUser):
    patient_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medical_record=models.TextField()

    def __str__(self):
        return f"Patient: {self.name}, ID: {self.patient_id}"
    
class Doctor(CustomUser):
    doctor_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    speciality= models.TextField()

    def __str__(self):
        return f"Doctor: {self.name}, ID: {self.doctor_id}"