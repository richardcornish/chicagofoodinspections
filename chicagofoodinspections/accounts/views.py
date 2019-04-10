from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import RegisterForm
from loglines.models import Logline

User = get_user_model()


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logline_list'] = Logline.objects.filter(user=self.request.user)
        return context


class PasswordView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = SetPasswordForm
    success_message = 'Password changed successfully.'
    template_name = 'accounts/password_form.html'
    success_url = reverse_lazy('accounts:password')


class LoginView(SuccessMessageMixin, LoginView):
    success_message = 'Logged in successfully.'
    template_name = 'accounts/login.html'


class LogoutView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
    pass


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:account')

    def form_valid(self, form):
        obj = form.save()
        obj = authenticate(**{
            User.USERNAME_FIELD: obj.get_username(),
            'password': form.cleaned_data['password']
        })
        login(self.request, obj)
        return super().form_valid(form)


class PasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    post_reset_login = True
    success_message = 'Password reset successfully.'
    success_url = reverse_lazy('accounts:account')
    template_name = 'accounts/password_reset_confirm.html'
