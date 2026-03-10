from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = Stats.objects.all()
        
        context['healers'] = Healer.objects.all()

        return context