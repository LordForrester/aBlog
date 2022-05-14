from django.shortcuts import render
# // we are importing this so we can use class based views
# Listview puts all are posts on the home page
# The detail view puts a single post onto a page
from django.views.generic import ListView, DetailView, CreateView

from.models import Post

#def home(request):
#    return render(request, 'home.html', {})


class HomeView(ListView):
    # here were are choosing our post model we made in the models.py
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'