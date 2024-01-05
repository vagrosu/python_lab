class InvalidCommandException(ValueError):
    """Exception thrown when an invalid command is provided to the application."""
    def __init__(self, message="Invalid command"):
        """
        Constructor for InvalidCommandException class.

        Attributes:
            message (str, optional): Explanation of the error.
        """
        self.message = message
