# Generated by Django 5.0.3 on 2024-03-31 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolidayMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MealDiet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
