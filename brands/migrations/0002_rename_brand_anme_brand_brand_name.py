# Generated by Django 5.0 on 2024-01-01 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='brand_anme',
            new_name='brand_name',
        ),
    ]