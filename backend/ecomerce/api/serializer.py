from rest_framework import serializers

from .models import Direction, Account, Followers, Complaints, Currency, Category, Image, Product, Image_Product, Status, Shipping_method, Payment_method, Order, Product_order, Payment_data, Action, Log, User_puntuation


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    direction = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Account
        fields = '__all__'

class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(many=True)
    followed = serializers.StringRelatedField(many=True)
    class Meta:
        model = Followers
        fields = ['id', 'follower', 'followed', 'follow_date']

class ComplaintSerializer(serializers.ModelSerializer):
    denounced_Account = serializers.StringRelatedField(many=True)
    accAccount_Account = serializers.StringRelatedField(many=True)
    class Meta:
        model = Complaints
        fields = ['id', 'date', 'denounced_Account', 'accAccount_Account']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Currency
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    currency = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)
    Account = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'currency', 'category', 'Account', 'date_created', 'date_updated']

class Image_ProductSerializer(serializers.ModelSerializer):
    image = serializers.StringRelatedField(many=True)
    product = serializers.StringRelatedField(many=True)
    class Meta:
        model = Image_Product
        fields = ['image', 'product']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_method
        fields = '__all__'

class paymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_method
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField(many=True)
    Shipping_method = serializers.StringRelatedField(many=True)
    Payment_method = serializers.StringRelatedField(many=True)
    direction = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Order 
        fields = ['id', 'status', 'subtotal', 'quantity', 'isv','total','direction','Shipping_method','Payment_method']

class Product_OrderSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)
    order = serializers.StringRelatedField(many=True)

    class Meta:
        model= Product_order
        fields= ['product','order']

class Payment_dataSerializer(serializers.ModelSerializer):
    Account = serializers.StringRelatedField(many=True)
    Payment_method = serializers.StringRelatedField(many=True)

    class Meta:
        model = Payment_data
        fields = ['id', 'Accountname','credit_card_number','expiration_date', 'cvv','Payment_method','Account','date_joined', 'date_updated']

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    Account = serializers.StringRelatedField(many=True)
    actions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Log
        fields = ['id', 'action','description','Account','actions']

class  User_puntuationSerializer(serializers.ModelSerializer):
    AccountSerializer = serializers.StringRelatedField(many=True)

    class Meta:
        model = User_puntuation
        fields = '__all__'

