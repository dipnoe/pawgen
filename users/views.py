from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        print(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST)
        try:
            send_mail(
                subject='Почта подтверждена',
                message='Добро пожаловать на PawGene! Вы успешно зарегистрировались на нашем сайте.',
                from_email=EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['email']]
            )
        except Exception as e:
            print(f'Не удалось отправить сообщение. Возникла ошибка {e}')
        finally:
            return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
