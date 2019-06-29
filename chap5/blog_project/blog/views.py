#blog/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView #new

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
# Create your views here.

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView): #new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']