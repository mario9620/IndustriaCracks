from rest_framework import viewsets

from .models import Direction, User, Followers, Complaints, Currency, Category, Image, Product, Image_Product, Status, shipping_method, payment_method, Order, product_order, payment_data, Action, Log
from .serializer import DirectionSerializer, UserSerializer, FollowerSerializer, ComplaintSerializer, CurrencySerializer, CategorySerializer, ImageSerializer, ProductSerializer, Image_ProductSerializer, StatusSerializer, ShippingMethodSerializer, paymentMethodSerializer, OrderSerializer, Product_OrderSerializer, Payment_dataSerializer, ActionSerializer, LogSerializer

class DirectionViewSet(viewsets.ModelViewSet):
    querysets = Direction.objects.all()
    serializer_class = DirectionSerializer

#Register user
class UserViewSet(viewsets.ModelViewSet):
    """
    Quería hacerlo con los métodos pero parece que con esas dos lineas 
    Django ya hace el crud
    @action(details=True, methods=['post'])
    def create(self, request):
        pass
    
    @action(details=True, methods=['put'])
    def updated(self, request, pk=None):
        pass
    
    @action(details=True, methods=['delete'])
    def destroy(self, request, pk=None):
        pass
    """
    querysets = User.objects.all()
    serializer_class = UserSerializer


class FollowersViewSet(viewsets.ModelViewSet):
    querysets = Followers.objects.all()
    serializer_class = FollowerSerializer

class ComplaintsViewSet(viewsets.ModelViewSet):
    querysets = Complaints.objects.all()
    serializer_class = ComplaintSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    querysets = Currency.objects.all()
    serializer_class = CurrencySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    querysets = Category.objects.all()
    serializer_class = CategorySerializer

class ImageViewSet(viewsets.ModelViewSet):
    querysets = Image.objects.all()
    serializer_class = ImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
    querysets = Product.objects.all()
    serializer_class = ProductSerializer

class ImageProductViewSet(viewsets.ModelViewSet):
    querysets = Image_Product.objects.all()
    serializer_class = Image_ProductSerializer

class StatusViewSet(viewsets.ModelViewSet):
    querysets = Status.objects.all()
    serializer_class = StatusSerializer

class ShippingMethodViewSet(viewsets.ModelViewSet):
    querysets = shipping_method.objects.all()
    serializer_class = ShippingMethodSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    querysets = payment_method.objects.all()
    serializer_class = paymentMethodSerializer

class OrderViewSet(viewsets.ModelViewSet):
    querysets = Order.objects.all()
    serializer_class = OrderSerializer

class Product_OrderViewSet(viewsets.ModelViewSet):
    querysets = product_order.objects.all()
    serializer_class = Product_OrderSerializer

class PaymentDataViewSet(viewsets.ModelViewSet):
    querysets = payment_data.objects.all()
    serializer_class = Payment_dataSerializer

class ActionViewSet(viewsets.ModelViewSet):
    querysets = Action.objects.all()
    serializer_class = ActionSerializer

class LogViewSet(viewsets.ModelViewSet):
    querysets = Log.objects.all()
    serializer_class = LogSerializer
