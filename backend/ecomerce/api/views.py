from django.shortcuts import render

# Create your views here.

from rest_framework import serializers
from .models import Account, Direction,Image,Followers, Puntuation, Complaints, Currency, Category,Product,Image_Product, Status, Shipping_method,Payment_data,Order,Product_order,Log
from .serializer import DirectionSerializer
from rest_framework import generics

from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin 

class DirectionGenericView(generics.GenericAPIView, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin):
    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):

        if not (id):
            return self.list(request)
        else:
            return self.retrieve(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id= None):
        return self.update(request, id)

    def delete(self, request, id = None):
        return self.destroy(request, id)