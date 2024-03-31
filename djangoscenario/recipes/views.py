from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe

def about(request):
    return render(request, 'recipes/about.html', {'title': 'about page'})

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'image', 'ingredients', 'method', 'meal_type', 'meal_diet', 'meal_holiday',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description','ingredients', 'method', 'meal_type', 'meal_diet', 'meal_holiday',]

    def test_func(self):
        recipe =self.get_object()
        return self.request.user ==recipe.author
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class NavbarRecipe(ListView):
    model = models.MealType
    template_name = 'recipes/base.html'
    context_object_name = 'mealtype'

    def get_names(self):
        return list(self.get_queryset().values_list('meal', flat=True))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = self.get_names()
        return context


