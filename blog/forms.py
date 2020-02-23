
from django import forms
from django.forms import ModelForm, Textarea
from .models import Blog


class UpdateBlog(ModelForm):
    class Meta:
        model   = Blog 
        fields  = ('title', 'body', 'author')
        widgets = {
            'body': Textarea(attrs={'cols':120,'rows':15}),
        }

