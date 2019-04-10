from django.contrib.auth.validators import ASCIIUsernameValidator


class SlugASCIIUsernameValidator(ASCIIUsernameValidator):
    regex = r'^[\w-]+\Z'
    message = 'Enter a valid username of letters, numbers, hyphens, or underscores.'
