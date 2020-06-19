class Message:
    """Message Class to hold the details of Message Sent"""
    def __init__(self, sender, receiver, message):
        """
        Args:
            sender (Kingdom Object): Message Sender Kingdom
            receiver (Kingdom Object): Message Receiver Kingdom
            message (string): Message that to be sent 
        """
        self.__sender = sender
        self.__receiver = receiver
        self.__message = message

    def get_sender(self):
        """Gets the Sender Kingdom Object of the Message
        Returns:
            Kingdom Object: Message Sender Kingdom
        """
        return self.__sender

    def get_receiver(self):
        """Gets the Receiver Kingdom Object of the Message
        Returns:
            Kingdom Object: Message Reciever Kingdom
        """
        return self.__receiver

    def get_message(self):
        """Gets the Message Text
        Returns:
            String: Message Text
        """
        return self.__message
