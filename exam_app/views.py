from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from exam_app.serializers import UserSerializer
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from exam_app.serializers import (
    ProductSerializer,
    OrderSerializer,
    UserSerializer,
    ProductVersionSerializer,
)
from exam_app.models import Product, Order, User, ProductVersion


class UserView(GenericViewSet,
               # mixins.ListModelMixin,
               mixins.CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProductVersionView(GenericViewSet,
               mixins.CreateModelMixin):
    serializer_class = ProductVersionSerializer
    queryset = ProductVersion.objects.all()


class ProductView(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderView(GenericViewSet,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer
    queryset = Order.objects.all()