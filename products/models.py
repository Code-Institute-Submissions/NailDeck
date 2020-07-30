from django.db import models
from django.core.validators import MaxValueValidator

#Products
class Product(models.Model):

    POLISHES = 'Polishes'
    CARE = 'Care'
    CHOICES = [
        (POLISHES, 'Polishes'),
        (CARE, 'Care'),
    ]
    name = models.CharField(max_length=254, default='Name')
    description = models.TextField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(
        max_length=20,
        choices=CHOICES, 
        default=POLISHES,
        )

    def __str__(self):
        return self.name