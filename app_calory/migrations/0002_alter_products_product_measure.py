# Generated by Django 4.2.5 on 2023-10-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_calory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="product_measure",
            field=models.CharField(
                choices=[
                    ("liter", "liter"),
                    ("gramm", "gramm"),
                    ("piece", "piece"),
                    ("spoon", "spoon"),
                    ("cup", "cup"),
                ],
                max_length=25,
                verbose_name="Measure",
            ),
        ),
    ]
