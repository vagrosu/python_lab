class IllegalArgumentException(ValueError):
    """Exception thrown when an invalid argument is provided to a command."""
    def __init__(self, message, command, errors=None):
        """
        Constructor for IllegalArgumentException class.

        Attributes:
            message (str): Explanation of the error.
            command (str): The command during which the error occurred.
            errors (list(str), optional): List of specific error details or reasons.
        """
        self.message = message
        self.command = command
        if errors is None:
            errors = []
        self.errors = errors
