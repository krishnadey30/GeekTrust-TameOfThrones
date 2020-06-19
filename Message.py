class Message:
    def __init__(self, sender, receiver, message):
        self.__sender = sender
        self.__receiver = receiver
        self.__message = message

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_message(self):
        return self.__message
