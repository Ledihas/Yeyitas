# Generated by Django 5.0.7 on 2024-07-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("terraza", "0002_bebidas_helados_platos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bebidas",
            name="alcohol",
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
