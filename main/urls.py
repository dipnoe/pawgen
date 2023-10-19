from django.urls import path

from main.apps import MainConfig
from main.views import *

app_name = MainConfig.name

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),

    path('service/list/<int:pk>/', ServiceListView.as_view(), name='service_category_list'),
    path('service/list/', ServiceAllListView.as_view(), name='service_all_list'),
    path('service/detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
]
