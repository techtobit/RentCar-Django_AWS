# Generated by Django 5.0 on 2024-01-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_rename_brand_anme_brand_brand_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]