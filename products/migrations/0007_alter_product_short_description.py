# Generated by Django 5.1 on 2024-09-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=100, verbose_name='Short Description'),
        ),
    ]
