def internal_error(e):
    return {"error": f"Internal server error: {str(e)}"}

def id_not_provided():
    return {"error": "Id not provided"}

def response_ok():
    return {"response": "ok"}


class IDNotFound(Exception):
    def __init__(self, base_message="Id not found", model=None, id=None, code=0):
        self.base_message = base_message
        self.model = model.__class__.__name__ if model else None
        self.code = code
        self.id = id
        super().__init__(self.__str__())

    def __str__(self):
        if self.model and self.id:
            return f"{self.base_message}: {self.model} '{self.id}' was not found. code={self.code}"
        return f"{self.base_message}. code={self.code}"

class InvalidReference(Exception):
    def __init__(self, base_message="Invalid reference", code=0, details=None):
        self.base_message = base_message
        self.details = details
        self.code = code
        super().__init__(self.__str__())

    def __str__(self):
        if self.details:
            return f"{self.base_message}: {self.details}. code={self.code}"
        return f"{self.base_message}. code={self.code}"

class AlreadyExists(Exception):
    def __init__(self, base_message="Already exists", code=0):
        self.base_message = base_message
        self.code = code
        super().__init__(self.__str__())

    def __str__(self):
        return f"{self.base_message}. code={self.code}"