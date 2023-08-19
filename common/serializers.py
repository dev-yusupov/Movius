from rest_framework.serializers import ModelSerializer

from .models import Contact, Catalog, Category

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'phone_number', 'email', 'address', 'city']
        read_only_fields = ['id']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']
    

class CatalogSerializer(ModelSerializer):
    contact = ContactSerializer()
    category = CategorySerializer()
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'description', "contact", "category"]
        read_only_fields = ['id']
    