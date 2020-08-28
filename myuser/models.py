from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=80, null=True, blank=True)
    

    def __str__(self):
        return self.username
