from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
import uuid

from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, APPROVE_URL
from order.models import Order
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        approval_code = uuid.uuid4().hex
        form.instance.approval_code = approval_code

        try:
            send_mail(
                subject='Подтверждение почты',
                message=f'Добро пожаловать на PawGene! Вы успешно зарегистрировались на нашем сайте.\n'
                        f'Для подтверждения почты перейдите по ссылке\n'
                        f'{APPROVE_URL}{form.instance.approval_code}',
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


def approve_email(request, approval_code):
    user_for_approve = get_object_or_404(User, approval_code=approval_code)
    user_for_approve.is_approved = True
    user_for_approve.approval_code = None

    content_type = ContentType.objects.get_for_model(Order)
    permission = Permission.objects.get(
        codename="set_status",
        content_type=content_type,
    )
    user_for_approve.user_permissions.add(permission)

    user_for_approve.save()
    return render(request, 'users/approve_email.html')
