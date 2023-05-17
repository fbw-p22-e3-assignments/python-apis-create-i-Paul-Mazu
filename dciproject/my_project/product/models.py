from django.db import models
import uuid


class Product(models.Model):
    product_name = models.CharField(max_length=200)  # (String)
    product_category = models.CharField(max_length=200)
    product_description = models.TextField(max_length=300)  # (String)
    product_image_url = models.ImageField(default="No_Image_Available.jpg")  # (String)
    product_price = models.PositiveIntegerField()  # (Integer)

    def __str__(self) -> str:
        return self.product_name
