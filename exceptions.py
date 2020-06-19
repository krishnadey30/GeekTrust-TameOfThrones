class Error(Exception):
    """Base class for other exceptions"""
    pass


class KingdomNotFound(Error):
    """Exception raised when Kindom is not found."""
    def __str__(self):
        return "Kindom not Found. Are you sure you are in correct planet?"

class InvalidAllyKingdom(Error):
    """Exception raised when Ally Kingdom is not valid."""
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


class InvalidMessageException(Error):
    """Exception raised when Invalid Message is sent."""
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message
