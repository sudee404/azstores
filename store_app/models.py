from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length = 64)
    price = models.DecimalField(decimal_places=2,max_digits=4)
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
