from django.urls import path
#from . import views

# because we are using class based views, we need to import each class view
from .views import HomeView, ArticleDetailView, AddPostView


urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),

    # when a new blog post is made, it is given a primary key, which is what we are calling bellow
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),

    path('add_post/', AddPostView.as_view(), name='add_post'),
]
