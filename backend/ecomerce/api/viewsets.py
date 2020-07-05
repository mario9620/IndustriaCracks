from rest_framework import viewsets

from .models import Direction, Account, Followers, Complaints, Currency, Category, Image, Product, Image_Product, Status, Shipping_method, Payment_method, Order, Product_order, Payment_data, Action, Log, User_puntuation
from .serializer import DirectionSerializer, AccountSerializer, FollowerSerializer, ComplaintSerializer, CurrencySerializer, CategorySerializer, ImageSerializer, ProductSerializer, Image_ProductSerializer, StatusSerializer, ShippingMethodSerializer, paymentMethodSerializer, OrderSerializer, Product_OrderSerializer, Payment_dataSerializer, ActionSerializer, LogSerializer, User_puntuationSerializer

class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

#Register Account
class AccountViewSet(viewsets.ModelViewSet):
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
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class FollowersViewSet(viewsets.ModelViewSet):
    queryset = Followers.objects.all()
    serializer_class = FollowerSerializer

class ComplaintsViewSet(viewsets.ModelViewSet):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ImageProductViewSet(viewsets.ModelViewSet):
    queryset = Image_Product.objects.all()
    serializer_class = Image_ProductSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class ShippingMethodViewSet(viewsets.ModelViewSet):
    queryset = Shipping_method.objects.all()
    serializer_class = ShippingMethodSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = Payment_method.objects.all()
    serializer_class = paymentMethodSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Product_OrderViewSet(viewsets.ModelViewSet):
    queryset = Product_order.objects.all()
    serializer_class = Product_OrderSerializer

class PaymentDataViewSet(viewsets.ModelViewSet):
    queryset = Payment_data.objects.all()
    serializer_class = Payment_dataSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class User_puntuationViewSet(viewsets.ModelViewSet):
    queryset = User_puntuation.objects.all()
    serializer_class = User_puntuationSerializer
