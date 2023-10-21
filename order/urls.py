from django.urls import path

from order.apps import OrderConfig
from order.views import OrderCreateView

app_name = OrderConfig.name

urlpatterns = [
   path('create/', OrderCreateView.as_view(), 'order_create'),
   path('update/<int:pk>/', OrderUpdateteView.as_view(), 'order_update'),
   path('list/', OrderCreateView.as_view(), 'order_list'),
   path('delete/', OrderDeleteView.as_view(), 'order_delete'),
]
