from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from main.forms import CategoryForm, ServiceForm
from main.models import Category, Service


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class ServiceListView(ListView):
    model = Service

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category'] = Category.objects.get(id=self.kwargs.get('pk'))
        return data

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ServiceAllListView(ListView):
    model = Service


class ServiceDetailView(DetailView):
    model = Service
