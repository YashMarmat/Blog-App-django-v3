
# username for this model is yashm

from django.db import models
from django.urls import reverse, reverse_lazy


class Blog(models.Model):
    title  = models.CharField(max_length = 120)
    body   = models.TextField(max_length = 3000)
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE, default = 1)
    #author  = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)
    
    def get_absolute_url(self):
        return reverse('blog_detail', args = [str(self.id)])

# i created this get_absolute_url so that after updation the user can get redirected to the
#  detail page, not on the list page. 
# Reason for creating this function is that, the blog_detail page needs blog id and we cannot
# mention that inside submit button class neither with the class of views.py beacause doing so
# leads to errors.  