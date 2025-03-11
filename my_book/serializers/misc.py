from rest_framework import serializers
from my_book.models import Product,Category,Review,ProductViewHistory
from django.db import models

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class ProductSerializers(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock','avg_rating']


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

class ProductViewHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductViewHistory
        fields="__all__"

