from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostModel

class BBList(ListView):
    template_name = 'top_page.html'
    model = PostModel

class BBDetail(DetailView):
    template_name = 'detail_page.html'
    model = PostModel