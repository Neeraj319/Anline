# Generated by Django 3.1 on 2021-01-23 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_product_announcement_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='announcement_type',
            new_name='product_type',
        ),
    ]