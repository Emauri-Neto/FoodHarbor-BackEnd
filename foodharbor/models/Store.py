from foodharbor.mixins.models import BaseModelMixin
from django.db import models
from authuser.models import User

class Store(BaseModelMixin):
    """
        Uma loja dentro do site
    """
    category = models.ForeignKey('StoreCategory', on_delete=models.CASCADE, blank=False, null=False)
    fantasy_name = models.CharField(max_length=20, unique=True, blank=False, null=False)
    social_reason = models.CharField(max_length=255, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    description = models.TextField()
    address = models.CharField(max_length=255,blank=False, null=False)

    def __str__(self):
        return self.fantasy_name + " - " + self.category.name
    
    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
        ordering = ["-created_at"]