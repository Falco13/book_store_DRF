from rest_framework import serializers
from book_store_app.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.category_title')

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'is_active', 'category']


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=25, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=25, min_length=7)
    first_name = serializers.CharField(max_length=15, min_length=3)
    last_name = serializers.CharField(max_length=15, min_length=3)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'This email is already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        user = User.objects.create_user(username=validated_data["username"],
                                        first_name=validated_data["first_name"],
                                        last_name=validated_data["last_name"],
                                        email=validated_data["email"],
                                        )
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
