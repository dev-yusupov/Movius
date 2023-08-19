from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ContactView, CatalogView, CategoryView

router = DefaultRouter()

router.register('contact', ContactView)
router.register('category', CategoryView)
router.register('catalog', CatalogView)

urlpatterns = [
    path('', include(router.urls))
]
