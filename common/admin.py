from django.contrib import admin

from .models import Category, Contact, Catalog

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'email', 'address', 'city']
    ordering = ['id']

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["name", 'contact', 'category']