from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    law_table = models.CharField(max_length=100)
    section_id = models.CharField(max_length=100)
    content = models.TextField()
    topic = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Note on {self.law_table} Section {self.section_id}"

