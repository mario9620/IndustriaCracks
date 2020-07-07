from django.urls import path
from .views import DirectionGenericView, AccountGenericView, ImageGenericView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('direction', DirectionGenericView, basename='direction')
router.register('account', AccountGenericView, basename='account')
router.register('image', ImageGenericView, basename='image')


from django.urls import path, include

urlpatterns = [
    path('viewset/', include(router.urls)),
]




