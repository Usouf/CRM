# Generated by Django 3.1.3 on 2020-12-09 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201129_1824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('change_product_price', 'can change product price only')]},
        ),
    ]
