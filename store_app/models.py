from django.db import models
from django.urls import reverse

# Create your models here.
TITLE_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unisex'),
]

class Product(models.Model):
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length = 64)
    price = models.PositiveIntegerField()
    description = models.TextField()
    gender = models.CharField(max_length=10, choices=TITLE_CHOICES)
    size = models.IntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})

class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=100)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name
