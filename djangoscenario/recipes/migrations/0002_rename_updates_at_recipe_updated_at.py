# Generated by Django 5.0.3 on 2024-03-20 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='updates_at',
            new_name='updated_at',
        ),
    ]
