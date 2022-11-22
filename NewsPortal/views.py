from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import NewsFilter


class PostsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'News.html'
    context_object_name = 'news'
    paginate_by = 1


class PostList(DetailView):
    model = Post
    template_name = 'Newsdetailed.html'
    context_object_name = 'news'


class PostsSearch(ListView):
    model = Post
    ordering = '-date'
    template_name = 'NewsSearch.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        if self.request.GET:
            context['filtered'] = True
        return context
