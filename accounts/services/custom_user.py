from django.contrib.auth import authenticate
from ..exceptions import MissingCredentials, InvalidCredentials
from ..forms import RegisterForm


class CustomUserService:
    def login(username, password):
        if not username or not password:
            raise MissingCredentials
        
        user = authenticate(None, username=username, password=password)
        if user is None:
            raise InvalidCredentials
        
        return user
    
    def create(**kwargs):
        for key, value in kwargs.items():
            if not value:
                raise MissingCredentials(key)
        
        form = RegisterForm(data=kwargs)
        if not form.is_valid():
            raise InvalidCredentials(details=form.errors.get_json_data())
        
        user = form.save()
        return user
