from django.shortcuts import render
from django.views.generic import TemplateView

class HomeEquipe(TemplateView):
    template_name = 'staff/home_equipe.html'