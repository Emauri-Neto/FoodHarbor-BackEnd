from django.db import models
from foodharbor.mixins.models import BaseModelMixin

class StoreCategory(BaseModelMixin):
    """
        Categoria de uma loja
    """
    name = models.CharField(max_length=30, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='StoreCategory'
        verbose_name_plural='StoreCaregories'
        ordering=['-name']