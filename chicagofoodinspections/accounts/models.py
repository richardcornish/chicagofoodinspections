from django.contrib.auth.models import AbstractUser

from .validators import SlugASCIIUsernameValidator


class User(AbstractUser):
    username_validator = SlugASCIIUsernameValidator()
