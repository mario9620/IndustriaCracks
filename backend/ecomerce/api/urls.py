from django.urls import path
from .views import DirectionGenericView, AccountGenericView, ImageGenericView, FollowGenericView, PuntuationGenericView, ComplaintsGenericView, CurrencyGenericView, CategoryGenericView, ProductGenericView, Image_productGenericView, StatusGenericView, ShipingGenericView, Payment_MethodGenericView, Payment_dataGenericView, OrderGenericView, Product_orderGenericView, LogGenericView, ActionGenericView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('direction', DirectionGenericView, basename='direction')
router.register('account', AccountGenericView, basename='account')
router.register('image', ImageGenericView, basename='image')
router.register('followers', FollowGenericView, basename='follower')
router.register('puntuation', PuntuationGenericView, basename='puntuation')
router.register('complaints', ComplaintsGenericView, basename='complaints')
router.register('currency', CurrencyGenericView, basename='currency')
router.register('category', CategoryGenericView, basename='category')
router.register('product', ProductGenericView, basename='product')
router.register('product_image', Image_productGenericView, basename='product_image')
router.register('status', StatusGenericView, basename='status')
router.register('shiping', ShipingGenericView, basename='shiping')
router.register('payment_method', Payment_MethodGenericView, basename='payment_method')
router.register('payment_data', Payment_dataGenericView, basename='payment_data')
router.register('order', OrderGenericView, basename='order')
router.register('product_order', Product_orderGenericView, basename='product_order')
router.register('action', ActionGenericView, basename='action')
router.register('log', LogGenericView, basename='log')




from django.urls import path, include

urlpatterns = [
    path('viewset/', include(router.urls)),
]




