from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('student', 'Law Student'),
        ('lawyer', 'Lawyer'),
        ('admin', 'Administrator'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='citizen')

    def __str__(self):
        return f"{self.user.username} Profile"
