from django.shortcuts import render
from django.views.generic import CreateView

from order.models import Order


# Create your views here.
class OrderCreateView(CreateView):
    model = Order
