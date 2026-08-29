from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='profile.role', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role')

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES, write_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'role')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        role = validated_data.pop('role', 'citizen')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        Profile.objects.create(user=user, role=role)
        return user
