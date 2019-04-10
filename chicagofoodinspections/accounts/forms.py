from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            User.USERNAME_FIELD,
            User.get_email_field_name(),
            'password',
        ]
        labels = {
            User.get_email_field_name(): 'Email',
        }
        help_texts = {
            User.USERNAME_FIELD: '',
        }
        widgets = {
            User.USERNAME_FIELD: forms.TextInput(attrs={
                'autocapitalize': 'off',
                'autocomplete': 'username',
                'autocorrect': 'off',
                'autofocus': True,
                'class': 'form-control form-control-lg',
            }),
            User.get_email_field_name(): forms.EmailInput(attrs={
                'autocapitalize': 'off',
                'autocomplete': 'home email',
                'autocorrect': 'off',
                'class': 'form-control form-control-lg',
            }),
            'password': forms.PasswordInput(attrs={
                'autocapitalize': 'off',
                'autocomplete': 'new-password',
                'autocorrect': 'off',
                'class': 'form-control form-control-lg',
            }),
        }

    def clean_username(self):
        username = self.cleaned_data[User.USERNAME_FIELD]
        return username.lower()

    def clean_email(self):
        email_field = User.get_email_field_name()
        email = self.cleaned_data[email_field]
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with that e-mail already exists.')
        return email.lower()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
