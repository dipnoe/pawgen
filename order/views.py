from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from order.forms import ApplicationForm
from order.models import Order, Application
from django.shortcuts import get_object_or_404


# Create your views here.
class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('order:application_list')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('order:application_list')


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    print(Application.service)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user.pk)
        return queryset


class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('order:application_list')


@permission_required('order.set_status')
def confirm(request, pk):
    object = get_object_or_404(Application, pk=pk)
    new_order = Order(
        user=object.owner,
        status='Submitted',
        amount=object.full_price()
    )
    new_order.save()
    new_order.service.set(object.service.all())
    new_order.save()

    if new_order.status == 'Submitted':
        object.is_submitted = True
        object.save()

    return redirect(reverse_lazy('order:application_list'))
