from django.shortcuts import render             # works for funtion based views
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # allows only logged in users to access website data
from django.core.exceptions import PermissionDenied  # author cannot update or delete the blogs made by other author.
from .forms import UpdateBlog


from django.views.generic import(
    ListView,
    DetailView,
)

from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView,
)

class BlogList(LoginRequiredMixin,ListView):
    model         = Blog
    template_name = "blog_list.html"
    login_url     = 'login'

class BlogDetail(LoginRequiredMixin, DetailView):
    model         = Blog
    template_name = "blog_detail.html"
    login_url     = 'login'

class BlogCreate(LoginRequiredMixin, CreateView):
    model          = Blog
    template_name  = "blog_new.html"
    form_class    = UpdateBlog                         # forms.py working here
    success_url    = reverse_lazy("blog_list")
    login_url      = 'login'
    
   
class BlogUpdate(LoginRequiredMixin, UpdateView):
    model         = Blog
    template_name = "blog_update.html"                   # forms.py working here
    form_class    = UpdateBlog                    
    login_url     = 'login'
    #success_url   = reverse_lazy("blog_detail")  # instead of using this method i created 
    # a function (in models.py) which will redirect us to the detail page (as we know it 
    # requires blog id to be get redirected.)

    # below, working on the module PermissionDenied

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogDelete(LoginRequiredMixin, DeleteView):
    model         = Blog
    template_name = "blog_delete.html"
    success_url   = reverse_lazy("blog_list")
    login_url     = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
