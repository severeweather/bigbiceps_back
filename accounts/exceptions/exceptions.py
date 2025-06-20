class MissingCredentials(Exception):
    def __init__(self, *args):
        self.missing = args
        super().__init__("Missing credentials")

class InvalidCredentials(Exception):
    def __init__(self, error):
        self.error = error
        super().__init__("Invalid credentials")