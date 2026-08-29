from django.db import models
from django.contrib.auth.models import User

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookmarks')
    title = models.CharField(max_length=255, blank=True, default='')
    law_table = models.CharField(max_length=100)
    section_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title or self.law_table} (Section {self.section_id})"

