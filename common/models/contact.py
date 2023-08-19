from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    phone_number = models.CharField(_("Phone Number"), max_length=17)
    email = models.EmailField(_("Email Address"))
    address = models.CharField(_("Address"), max_length=100)
    city = models.CharField(_("City"), max_length=100)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    
    def __str__(self):
        return f"{self.address} ({self.city})"

    