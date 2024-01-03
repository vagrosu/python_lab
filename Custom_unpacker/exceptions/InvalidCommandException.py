class InvalidCommandException(ValueError):
    def __init__(self, message="Invalid command"):
        self.message = message
