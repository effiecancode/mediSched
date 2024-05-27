from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='authentication/login.html', success_url='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
]
