from django.db import models 
from django.utils.translation import gettext_lazy as _

class Catalog(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField()
    contact = models.ForeignKey("common.Contact", on_delete=models.CASCADE, related_name="contacts")
    category = models.ForeignKey("common.Category", on_delete=models.CASCADE, related_name="categories")

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"

    def __str__(self):
        return f"{self.name}"