from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','email','password','role','contact_info')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data.get('email'), password=validated_data['password'], role=validated_data.get('role','customer'), contact_info=validated_data.get('contact_info',''))
        return user
