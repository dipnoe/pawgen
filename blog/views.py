from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Blog


# Create your views here.
class BlogView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
