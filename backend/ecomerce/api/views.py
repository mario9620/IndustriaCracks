from django.shortcuts import render

# Create your views here.
from .models import Account, Direction,Image,Followers, Puntuation, Complaints, Currency, Category,Product,Image_Product, Status, Shipping_method,Payment_data,Order,Product_order,Log

from rest_framework import serializers
from .serializer import DirectionSerializer, AccountSerializer, ImageSerializer

from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin 

class DirectionGenericView(viewsets.GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin):
    serializer_class = DirectionSerializer
    queryset = Direction.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):

        if not (id):
            return self.list(request)
        else:
            return self.retrieve(request)

    def post(self, request, id= None):
        return self.create(request)
    
    def put(self, request, id= None):
        return self.update(request, id)

    def delete(self, request, id= None):
        return self.destroy(request, id)


class AccountGenericView(viewsets.GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):

        if not (id):
            return self.list(request)
        else:
            return self.retrieve(request)

    def post(self, request,id=None):
        return self.create(request)

    def put(self, request, id= None):
        return self.update(request, id)

    def delete(self, request, id = None):
        return self.destroy(request, id)

class ImageGenericView(viewsets.GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):

        if not (id):
            return self.list(request)
        else:
            return self.retrieve(request)

    def post(self, request,id=None):
        return self.create(request)

    def put(self, request, id= None):
        return self.update(request, id)

    def delete(self, request, id = None):
        return self.destroy(request, id)