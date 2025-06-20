from django.urls import path
from .views.account_login import AccountLoginView
from .views.account_register import AccountRegisterView
from .views.account_logout import AccountLogoutView
from .views.auth_session import AuthSession

urlpatterns = [
    path('status/', AuthSession.as_view(), name="account__status"),
    path('register/', AccountRegisterView.as_view(), name='account__register'),
    path('login/', AccountLoginView.as_view(), name='account__login'),
    path('logout/', AccountLogoutView.as_view(), name='account__logout'),
]