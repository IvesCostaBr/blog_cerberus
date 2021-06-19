from apps.category.models import Category
from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.

class CategoryList(ListView):
    model = Category
    