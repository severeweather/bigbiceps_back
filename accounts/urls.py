from django.urls import path
from .views.account_login import AccountLoginView
from .views.account_register import AccountRegisterView
from .views.auth_session import AuthSession

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='accounts__register'),
    path('login/', AccountLoginView.as_view(), name='accounts__login'),
    # path('logout/', log_out, name='logout'),
    path('status/', AuthSession.as_view(), name="accounts__status")
]