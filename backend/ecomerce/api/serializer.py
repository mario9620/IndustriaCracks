from rest_framework import serializers

from .models import Direction, User, Followers, Complaints, Currency, Category, Image, Product, Image_Product, Status, shipping_method, payment_method, Order, product_order, payment_data, Action, Log


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    direction = serializers.StringRelatedField(many=True)
    class Meta: 
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'birth_date', 'is_admin', 'is_superuser','user_image','cover_image', 'join_date', 'direction']

class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(many=True)
    followed = serializers.StringRelatedField(many=True)
    class Meta:
        model = Followers
        fields = ['id', 'follower', 'followed', 'follow_date', 'puntuation']

class ComplaintSerializer(serializers.ModelSerializer):
    denounced_User = serializers.StringRelatedField(many=True)
    accuser_User = serializers.StringRelatedField(many=True)
    class Meta:
        model = Complaints
        fields = ['id', 'date', 'denounced_User', 'accuser_User']

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
    user = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'currency', 'category', 'user', 'date_created', 'date_updated']

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
        model = shipping_method
        fields = '__all__'

class paymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_method
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField(many=True)
    shipping_method = serializers.StringRelatedField(many=True)
    payment_method = serializers.StringRelatedField(many=True)
    direction = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Order 
        fields = ['id', 'status', 'subtotal', 'quantity', 'isv','total','direction','shipping_method','payment_method']

class Product_OrderSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)
    order = serializers.StringRelatedField(many=True)

    class Meta:
        model= product_order
        fields= ['product','order']

class Payment_dataSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True)
    payment_method = serializers.StringRelatedField(many=True)

    class Meta:
        model = payment_data
        fields = ['id', 'username','credit_card_number','expiration_date', 'cvv','payment_method','user','date_joined', 'date_updated']

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True)
    actions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Log
        fields = ['id', 'action','description','user','actions']

