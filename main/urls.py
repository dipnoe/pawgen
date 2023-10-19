from django.urls import path

from main.apps import MainConfig
from main.views import *

app_name = MainConfig.name

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('category/list/', CategoryListView.as_view(), name='list_category'),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='detail_category'),

    path('create/', ServiceCreateView.as_view(), name='create_service'),
    path('update/<int:pk>/', ServiceUpdateView.as_view(), name='update_service'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete_service'),
    path('list/', ServiceListView.as_view(), name='list_service'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='detail_service'),
]
