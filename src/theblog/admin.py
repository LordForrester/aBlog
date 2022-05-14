from django.contrib import admin
from .models import Post

#this will allow all blog posts to be accesable from the admin page
admin.site.register(Post)

