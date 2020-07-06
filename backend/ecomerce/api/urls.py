from django.urls import path
from .views import DirectionGenericView

urlpatterns = [
    path('Direction/<str:id>/', DirectionGenericView.as_view()),
    path('Direction/', DirectionGenericView.as_view()),
    
]

