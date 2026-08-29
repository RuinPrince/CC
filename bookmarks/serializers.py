from rest_framework import serializers
from .models import Bookmark, Folder

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'
        read_only_fields = ('user',)

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
        read_only_fields = ('user',)
