from django.urls import path
from .views import DirectionGenericView, AccountGenericView, ImageGenericView

urlpatterns = [
    path('Direction/<str:id>/', DirectionGenericView.as_view()),
    path('Direction/', DirectionGenericView.as_view()),
    path('Account/<str:id>/', AccountGenericView.as_view()),
    path('Account/',AccountGenericView.as_view()),
    path('Image/<str:id>/', ImageGenericView.as_view()),
    path('Image/',ImageGenericView.as_view()),
    
]

