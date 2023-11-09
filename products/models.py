from django.conf import settings
from django.db import models
from django.utils import timezone

from django.utils.text import slugify 


# Define the Product Model
class Product(models.Model):
    # Defining the model's fields (the columns in the database)
    category = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    # Linked to another model
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
#   image
#   thumbnail
    date_added = models.DateTimeField(auto_now_add=True)

    # The methods of this Model

    # Automatically generate the slug based off the name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name