from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, DeleteView, UpdateView
from django.utils import timezone
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Blog
from .forms import BlogForm

class BlogListView(FormMixin, ListView):
    model = Blog
    template_name = 'blog.html'
    form_class = BlogForm
    context_object_name = 'blog_data'
    success_url = reverse_lazy('blog')
    ordering = ['-created_at']

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object_list = self.get_queryset()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.created_at = timezone.now().today()
        blog.updated_at = timezone.now().today()
        blog.views = 0
        blog.is_published = True
        blog.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class BlogDeleteView(DeleteView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('blog')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog_info'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views = F('views') + 1
        obj.save(update_fields=['views'])

        return obj


class BlogUpdateView(UpdateView, LoginRequiredMixin):
    model = Blog
    template_name = 'blog_update.html'
    fields = ['header', 'content', 'preview_image']
    context_object_name = 'blog_info'
    success_url = reverse_lazy('blog')

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.updated_at = timezone.now().today()
        obj.save(update_fields=['updated_at'])

        return super().post(request, *args, **kwargs)