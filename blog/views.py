from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog_data'

