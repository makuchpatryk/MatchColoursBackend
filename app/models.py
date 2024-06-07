from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.CharField(max_length=250, unique=False, null=False, blank=False)
    REGISTRATION_CHOICES = [
        ('google', 'Google'),
        ('github', 'Github'),
    ]
    registration_method = models.CharField(
        max_length=10,
        choices=REGISTRATION_CHOICES,
        default='email'
    )

    def __str__(self):
       return self.username