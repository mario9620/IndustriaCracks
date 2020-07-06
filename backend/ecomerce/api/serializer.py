from rest_framework import serializers
from .models import Account, Direction,Image,Followers, Puntuation, Complaints, Currency, Category,Product,Image_Product, Status, Shipping_method,Payment_data,Order,Product_order,Log

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Direction
        fields= '__all__'
