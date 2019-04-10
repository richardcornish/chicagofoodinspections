from django.urls import path

from .views import ProfileDetailView, ProfileListView


app_name = 'profiles'

urlpatterns = [
    # path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('<slug:username>/', ProfileDetailView.as_view(), name='profile_detail'),
]
