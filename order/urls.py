from django.urls import path

from order.apps import OrderConfig
from order.views import ApplicationCreateView, ApplicationListView, ApplicationDeleteView, ApplicationUpdateView, \
    confirm

app_name = OrderConfig.name

urlpatterns = [
    path('application/create/', ApplicationCreateView.as_view(), name='application_create'),
    path('application/update/<int:pk>', ApplicationUpdateView.as_view(), name='application_update'),
    path('application/list/', ApplicationListView.as_view(), name='application_list'),
    path('application/delete/<int:pk>', ApplicationDeleteView.as_view(), name='application_delete'),

    path('application/confirm/<int:pk>', confirm, name='application_confirm')
]
