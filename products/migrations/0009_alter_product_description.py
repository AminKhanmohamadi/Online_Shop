# Generated by Django 5.1 on 2024-09-02 13:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
    ]
