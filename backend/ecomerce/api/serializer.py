from rest_framework import serializers
from .models import Account, Direction,Image,Followers, Puntuation, Complaints, Currency, Category,Product,Image_Product, Status, Shipping_method,Payment_data,Order,Product_order,Log

class DirectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Direction
        fields= '__all__'

class AccountSerializer(serializers.ModelSerializer):
    direction = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Account
        fields= '__all__'
        read_only_fields = ('date_joined','last_login')

class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Image
        fields= '__all__'
