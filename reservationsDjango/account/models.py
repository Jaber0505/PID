from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class CustomUser(AbstractUser):
    objects = CustomUserManager()

    def natural_key(self):
        return (self.username,)