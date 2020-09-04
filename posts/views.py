from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView): # internally Listview returns an object called object_list that we want to display in out template
    model = Post
    template_name = 'home.html'
