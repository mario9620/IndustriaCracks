from rest_framework import serializers
from .models import Account, Direction,Image,Followers, Puntuation, Complaints, Currency, Category,Product,Image_Product, Status, Shipping_method, Payment_method ,Payment_data,Order,Product_order,Log, Action

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

class FollowersSerializar(serializers.ModelSerializer):
    class Meta():
        model = Followers
        fields='__all__'

class PuntuationSerializer(serializers.ModelSerializer):
    class Meta():
        model= Puntuation
        fields= '__all__'

class ComplaintsSerializaer(serializers.ModelSerializer):
    class Meta():
        model = Complaints
        fields='__all__'

class CurrencySerializaer(serializers.ModelSerializer):
    class Meta():
        model = Currency
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model= Category
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model =Product
        fields='__all__'

class Image_ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Image_Product
        fields='__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta():
        model = Status
        fields='__all__'

class ShipingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Shipping_method
        fields='__all__'

class Payment_methodSerializer(serializers.ModelSerializer):
    class Meta():
        model = Payment_method
        fields='__all__'

class Payment_dataSerializer(serializers.ModelSerializer):
    class Meta():
        model = Payment_data
        fields='__all__'

#Order,Product_order,Log
class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields='__all__'

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product_order
        fields='__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta():
        model = Log
        fields='__all__'


class ActionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Action
        fields='__all__'