from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'matiangi'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('accounts/login/', views.login_page, name='login_page'),
    path('accounts/register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
]