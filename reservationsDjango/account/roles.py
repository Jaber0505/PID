from django.db import models
from django.conf import settings

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "account_role"

    def __str__(self):
        return self.name


class RoleUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = "account_roleuser"
        unique_together = ("user", "role")

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"
