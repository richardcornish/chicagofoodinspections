from django.views.generic import DetailView, ListView

from .models import Profile


class ProfileListView(ListView):
    model = Profile


class ProfileDetailView(DetailView):
    model = Profile
    slug_field = 'user__username'
    slug_url_kwarg = 'username'
