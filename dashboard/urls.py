from django.urls import path, re_path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('posts', views.posts, name="posts"),
]