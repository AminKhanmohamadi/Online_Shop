# Generated by Django 5.1 on 2024-09-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug'),
        ),
    ]
