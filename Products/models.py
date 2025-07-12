from django.db import models

class Product (models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)
    price = models.PositiveIntegerField(blank=False, null=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
