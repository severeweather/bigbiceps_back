from django.contrib.auth import authenticate
from ..exceptions.exceptions import MissingCredentials, InvalidCredentials


class CustomUserService:
    def get_form_data():
        pass

    def login(username, password):
        if not username or not password:
            raise MissingCredentials
        
        user = authenticate(None, username=username, password=password)
        if user is None:
            raise InvalidCredentials
        
        return user