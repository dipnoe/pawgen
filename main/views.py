from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from main.forms import CategoryForm, ServiceForm
from main.models import Category, Service


# Create your views here.
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('core:home')


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('core:home')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('core:home')


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('core:home')


class ServiceListView(ListView):
    model = Service


class ServiceDetailView(DetailView):
    model = Service


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('core:home')


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('core:home')
