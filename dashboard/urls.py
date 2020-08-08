from django.urls import path, re_path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    re_path(r'^posts/(?P<page_id>[0-9_]+)/$', views.posts, name="posts"),
    re_path(r'^post/(?P<id>[0-9_]+)/$', views.post_view, name="postview"),
    path('post/analyze_post', views.analyze_post, name="analyzepost"),
    path('post/generate_csv', views.generate_csv, name="generatecsv"),
    path('search_page', views.searchpage, name="searchpage")
]