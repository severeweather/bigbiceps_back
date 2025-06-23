class MissingCredentials(Exception):
    def __init__(self, base_message="Missing credentials", *credentials):
        self.credentials = credentials
        self.base_message = base_message
        super().__init__(self.__str__())

    def __str__(self):
        if self.credentials:
            return f"{self.base_message}: {self.credentials}"
        return self.base_message 

class InvalidCredentials(Exception):
    def __init__(self, base_message="Invalid credentials", details=None):
        self.details = details
        self.base_message = base_message
        super().__init__(self.__str__())

    def __str__(self):
        if self.details:
            return f"{self.base_message}: {self.details}"
        return self.base_message 