from django.urls import path

from .views import (
    AccountView,
    LoginView,
    LogoutView,
    PasswordView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    RegisterView,
)


app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('password/', PasswordView.as_view(), name='password'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', AccountView.as_view(), name='account'),
]
