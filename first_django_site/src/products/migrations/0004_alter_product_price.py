# Generated by Django 4.1.7 on 2023-04-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.TextField(),
        ),
    ]
