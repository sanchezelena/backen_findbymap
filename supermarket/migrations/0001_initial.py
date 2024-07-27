# Generated by Django 5.0.7 on 2024-07-27 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="categories/")),
            ],
        ),
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
                ("product_name", models.CharField(max_length=100)),
                ("barcode", models.CharField(max_length=100, unique=True)),
                ("units", models.IntegerField()),
                ("image", models.ImageField(upload_to="products/")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("offert", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Ubication",
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
                ("aisle", models.CharField(max_length=100)),
                ("shelf", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
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
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="supermarket.category",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="supermarket.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="categories",
            field=models.ManyToManyField(
                through="supermarket.ProductCategory", to="supermarket.category"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="ubication",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="supermarket.ubication"
            ),
        ),
    ]