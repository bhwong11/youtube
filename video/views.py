from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from .models import Video

# Create your views here.
class Feed(TemplateView):
    template_name= 'videos/feed.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context
        #DTL don't invoke methods
        #get_context_data method passes all default info like user information and passes them forward