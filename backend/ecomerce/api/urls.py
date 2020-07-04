from rest_framework import routers 

from .viewsets import DirectionViewSet, UserViewSet, FollowersViewSet, ComplaintsViewSet, CurrencyViewSet, CategoryViewSet, ImageViewSet, ProductViewSet, ImageProductViewSet, StatusViewSet, ShippingMethodViewSet, PaymentMethodViewSet, OrderViewSet, Product_OrderViewSet, PaymentDataViewSet, ActionViewSet, LogViewSet

#Las rutas de tablas intermedias no las agrege

router = routers.SimpleRouter()
router.register('direction', DirectionViewSet, basename='direction')
router.register('users', UserViewSet, basename='users')
router.register('followers', FollowersViewSet, basename='followers')
router.register('complaints', ComplaintsViewSet, basename='complaints')
router.register('currencies', CurrencyViewSet, basename='currencies')
router.register('categories', CategoryViewSet, basename='categories')
router.register('images', ImageViewSet, basename='images')
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('payments', PaymentDataViewSet, basename='payments')
router.register('actions', ActionViewSet, basename='actions')
router.register('logs', LogViewSet, basename='logs')

urlpatterns = router.urls
