from django.urls import path
from . import views, forms

app_name = 'accounts'

urlpatterns = [
    path('signin/', views.signin , name='signin'),
    path('logout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
]
