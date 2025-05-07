from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class AppUserManager(BaseUserManager):
    def create_user(self, email, name,phone, age, gender, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field is mandatory')       
        # converting email with lower case
        email= self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone=phone,
            age= age,
            gender= gender,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
   
    def create_superuser(self, email, name, phone, age, gender, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if not password:
            raise ValueError("Superusers must have a password.")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, name, phone, age, gender, password, **extra_fields)


class AppUser(AbstractUser):


    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    # redefine the email to be unique
    email = models.EmailField(unique=True)

    ROLE_CHOICES = (
    ('user', 'User'),
    ('admin', 'Admin'),
    # add more roles as needed
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    # Adding extra field  inside the custom user class
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # removing the username field
    username= None
    objects = AppUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'age', 'gender']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='appuser_groups',  # Unique reverse accessor name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='appuser_permissions',  # Unique reverse accessor name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email
