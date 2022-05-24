from django.db import models
#this imports the super user we created in django admin
from django.contrib.auth.models import User
from django.urls import reverse


# Remember, when making changes to this database, run 'manage.py makemigrations"
# and run 'manage.py migrate"
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="MySweet Blog")
    # this deletes all posts from the user if the user is removed from database
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    # on the admin page, this will allow us to see the title and author of a post
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # we are naming method 'get_absolute_url' because if we try making a new post via the add_post page, we will have an error requesting the get_absolute_url method
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')