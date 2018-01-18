from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse
from exam_app.models import (
    Order,
    Category,
    Product,
    ProductVersion,
)


class CategoryCreatedForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ()


class CategoryCreated(admin.ModelAdmin):
    form = CategoryCreatedForm
    list_display = ('name',)
    search_fields = ('name',)


class ProductCreatedForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()


class ProductCreated(admin.ModelAdmin):
    form = ProductCreatedForm
    list_display = ('name', 'category',)
    search_fields = ('name', 'category',)

    # def get_categories(self, obj):
    #     link = reverse()


class ProductVersionCreatedForm(forms.ModelForm):
    class Meta:
        model = ProductVersion
        exclude = ()


class ProductVersionCreated(admin.ModelAdmin):
    form = ProductVersionCreatedForm
    list_display = ('name', 'price',)
    search_fields = ('name', 'price',)


admin.site.register(Order)
admin.site.register(Category, CategoryCreated)
admin.site.register(Product, ProductCreated)
admin.site.register(ProductVersion, ProductVersionCreated)