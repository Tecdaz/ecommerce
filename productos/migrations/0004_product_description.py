# Generated by Django 5.0.6 on 2024-07-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_remove_product_colour_remove_product_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.TextField(default='Sin descripcion'),
            preserve_default=False,
        ),
    ]