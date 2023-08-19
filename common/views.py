from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import ContactSerializer, CategorySerializer, CatalogSerializer
from .models import Contact, Category, Catalog

# Create your views here.
class ContactView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [AllowAny,]

class CatalogView(ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()
    permission_classes = [AllowAny,]

class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny,]