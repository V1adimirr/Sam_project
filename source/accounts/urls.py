from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from source.accounts.views import MyRegisterView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', MyRegisterView.as_view(), name='registration'),
]
