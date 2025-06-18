from django.urls import path
from .views.account_login import AccountLoginView

urlpatterns = [
    # path('register/', register, name='register'),
    path('login/', AccountLoginView.as_view(), name='accounts__login'),
    # path('logout/', log_out, name='logout'),
]