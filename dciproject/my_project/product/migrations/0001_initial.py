# Generated by Django 4.2.1 on 2023-05-17 11:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=200)),
                (
                    "product_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("product_category", models.CharField(max_length=200)),
                ("product_description", models.TextField(max_length=300)),
                ("product_image_url", models.ImageField(upload_to="")),
                ("product_price", models.PositiveIntegerField()),
            ],
        ),
    ]
