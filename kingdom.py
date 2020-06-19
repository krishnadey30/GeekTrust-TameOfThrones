from exceptions import KingdomNotFound, InvalidAllyKingdom, InvalidMessageException
from MessageVerify import MessageVerify
from Message import Message

class Kingdom:
    """Class Kindom, holds all the details of a Kingdom in Southeros"""

    __kingdoms = dict()    # static variable to hold the list of all the kingdoms of Southeros
    def __init__(self, name, emblem):
        """
        Args:
            name (string): The first parameter. Name of the Kingdom
            emblem (string): The second parameter. Emblem of the Kingdom.
        """
        self.__kingdom_name = name
        self.__kingdom_emblem = emblem
        self.__ally_kingdoms = set()
        Kingdom.__add_kingdom(self)
    
    @classmethod
    def get_kingdom(cls, name):
        """Class Method to get Kingdom Object from Name of Kingdom 
        Args:
            name (string): name of the Kingdom
        
        Returns:
            Kingdom Object: Kingdom Object for the given name
        Raises:
            KingdomNotFound:
                If no Kingdom is found for the kingdom name passed in as a parameter.
        """
        if name in cls.__kingdoms.keys():
            return cls.__kingdoms[name]
        else:
            raise KingdomNotFound
    
    @classmethod
    def __add_kingdom(cls, kingdom):
        """Class Method to add Kingdom Object to the list of Kingdoms
        Args:
            kingdom (object): Kingdom Object to be added
        """
        cls.__kingdoms[kingdom.name()] = kingdom
    
    def get_allies(self):
        """Returns the list of Allies the Kingdom has
        Returns:
            list: The name of all kingdoms which are allies to the Kingdom
        """
        allies = []
        for kingdom in self.__ally_kingdoms:
            allies.append(kingdom.name())
        return allies
    
    def name(self):
        """Get the name of the kingdom
        Returns:
            string: Name of the Kingdom
        """
        return self.__kingdom_name
    
    def emblem(self):
        """Get the emblem of the kingdom
        Returns:
            string: Emblem of the Kingdom
        """
        return self.__kingdom_emblem

    def emblem_length(self):
        """Get the length of emblem of the kingdom
        Returns:
            int: Size of the Emblem of Kingdom
        """
        return len(self.emblem())
    
    def add_ally(self, otherKingdom):
        """Adds the passed kingdom ally of the caller Kingdom

        Args:
            otherKingdom (Object): Kindom object to be ally
        Raises:
            InvalidAllyKingdom: If the to be Ally Kingdom is not valid for making Ally
        """
        if otherKingdom.name() == None:
            raise KingdomNotFound
        elif otherKingdom == self:
            raise InvalidAllyKingdom("Cannot add itself as ally")
        else:
            if not self.is_ally(otherKingdom):
                self.__ally_kingdoms.add(otherKingdom)
                otherKingdom.add_ally(self)

    def is_ally(self, otherKingdom):
        """Checks if the passed Kingdom is ally of the Caller Kingdom
        
        Args:
            otherKingdom (object): Kingdom to be checked
        Returns:
            bool: True if is an Ally, False otherwise.
        """
        return otherKingdom in self.__ally_kingdoms

    def total_allies(self):
        """Return the total count of Allies a Kingdom has
        
        Returns:
            int: Count of Allies
        """
        return len(self.__ally_kingdoms)

    def send_message(self, message):
        """Sends Message to Other Kingdom. If the message response if True,
                Adds the both sender and reciever Kingdoms as Allies 
        
        Args:
            message (Message Object): Message Object
        Returns:
            bool: True if the response is positive, False Otherwise
        """
        otherKingdom = message.get_receiver()
        if otherKingdom == self:
            raise InvalidMessageException("Cannot send message to itself")
        
        response = MessageVerify.verify(otherKingdom, message.get_message())
        
        if response:
            self.add_ally(otherKingdom)
        
        return response

    def is_ruler(self):
        """Checks if the Kingdom is a ruling Kingdom
        Returns:
            bool: True if the kingdom is a ruling Kingdom, False otherwise
        """
        return self.total_allies() >= 3

    @classmethod
    def get_all(cls):
        """Class Method to iterate over all the Kingdoms
        Yields:
            `Kingdom Object`: The Kingdom Objects one by one
        """
        for kingdom_name in cls.__kingdoms.keys():
            yield cls.__kingdoms[kingdom_name]
        
    @classmethod
    def get_ruler(cls):
        """Class Method to get the Ruler of all Kingdoms
        
        Returns:
            `Kingdom Object`: Ruler Kingdom if it exists, None Otherwise
        """
        for kingdom in cls.get_all():
            if kingdom.is_ruler():
                return kingdom
        return None
    
    @classmethod
    def remove_all_kingdoms(cls):
        """Removes all the Kingdoms"""
        for kingdom in cls.get_all():
            del kingdom
        cls.__kingdoms.clear()

    

