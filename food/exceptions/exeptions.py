class IDNotFound(Exception):
    def __init__(self, model, id):
        self.model = model.__class__.__name__
        self.id = id
        super().__init__(f"{model} with ID {id} was not found")

class InvalidReference(Exception):
    pass

class MissingField(Exception):
    pass

class AlreadyExists(Exception):
    pass