# Generated by Django 5.0.3 on 2024-03-31 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_updates_at_recipe_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to='recipe_images'),
        ),
    ]