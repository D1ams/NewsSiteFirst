from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'News.html'
    context_object_name = 'news'


class PostList(DetailView):
    model = Post
    template_name = 'Newsdetailed.html'
    context_object_name = 'news'


