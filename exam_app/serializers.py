from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from exam_app.models import (
    Order,
    Category,
    Product,
    ProductVersion,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ProductVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion
        exclude = ()



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'last_login',
            'date_joined',
            'is_active',
            'groups',
            'user_permissions',
        )

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=make_password(validated_data['password'])
        )

        user.set_password(validated_data['password'])
        user.save()

        return user