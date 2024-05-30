from django.urls import path
from .views import UserProfileListCreateView

urlpatterns = [
    path("newuser/", UserProfileListCreateView.as_view(), name="user-profile")
]