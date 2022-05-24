#our forms.py is for formatting user input boxes and selectors
from django import forms
#first we need to call our post model
from .models import Post

# the paramter "forms" is from out forms import above, and we are using ".ModelForm" becuase our database has a model in the models.py file, the "Post" Model
class PostForm(forms.ModelForm):
    class Meta:
        #here we are assigning our "Post" model in the model.py file to the variable "model" below
        model = Post
        #here we are setting our fields variable to each of the fields in our "Post" model in models.py
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            # here we assign widgets to each of our form fields so we can cuztomize them
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

    }