from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class MealType(models.Model):
    meal = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.meal

class MealDiet(models.Model):
    diet = models.CharField(max_length=50)

    def __str__(self):
        return self.diet
    
class HolidayMeal(models.Model):
    holiday = models.CharField(max_length=50)

    def __str__(self):
        return self.holiday

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="recipe_images", null=True) 

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})


    def __str__(self):
        return self.title