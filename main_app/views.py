from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'