# Generated by Django 4.2.5 on 2023-10-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
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
                    "product_name",
                    models.CharField(max_length=255, verbose_name="Food name"),
                ),
                (
                    "product_amount",
                    models.IntegerField(verbose_name="Food amount (100)"),
                ),
                (
                    "product_measure",
                    models.CharField(
                        choices=[
                            ("piece", "piece"),
                            ("cup", "cup"),
                            ("gramm", "gramm"),
                            ("liter", "liter"),
                            ("spoon", "spoon"),
                        ],
                        max_length=25,
                        verbose_name="Measure",
                    ),
                ),
                ("product_calory", models.IntegerField(verbose_name="Product calory")),
                ("product_fat", models.IntegerField(verbose_name="Product fat")),
                (
                    "product_protein",
                    models.IntegerField(verbose_name="Product protein"),
                ),
                ("product_carbs", models.IntegerField(verbose_name="Product carbs")),
                ("product_fiber", models.IntegerField(verbose_name="Product fiber")),
                ("product_sugar", models.IntegerField(verbose_name="Product sugar")),
            ],
            options={
                "db_table": "products",
            },
        ),
    ]
