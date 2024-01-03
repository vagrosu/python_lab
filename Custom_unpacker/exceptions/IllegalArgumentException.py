class IllegalArgumentException(ValueError):
    def __init__(self, message, command, errors=None):
        self.message = message
        self.command = command
        if errors is None:
            errors = []
        self.errors = errors
