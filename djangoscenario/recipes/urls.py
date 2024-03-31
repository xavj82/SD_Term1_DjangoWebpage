from django.urls import path
from . import views
from .views import meal_display

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes-home'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('recipes/meals/<int:meal_id>/', meal_display, name="recipes-recipes"),
]