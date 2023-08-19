from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("Name of Category"), max_length=100)
    description = models.TextField(_("Description of category"))

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    
    def __str__(self):
        return f"{self.name}"