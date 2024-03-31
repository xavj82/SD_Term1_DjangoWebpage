from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Recipe)
admin.site.register(models.MealDiet)
admin.site.register(models.MealType)
admin.site.register(models.HolidayMeal)