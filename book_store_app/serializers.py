from rest_framework import serializers
from book_store_app.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.category_title')

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'is_active', 'category']


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
