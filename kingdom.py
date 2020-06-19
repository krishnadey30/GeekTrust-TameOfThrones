from exceptions import KingdomNotFound, InvalidAllyKingdom, InvalidMessageException
from MessageVerify import MessageVerify
from Message import Message

class Kingdom:
    __kingdoms = dict()
    def __init__(self, name, emblem):
        self.__kingdom_name = name
        self.__kingdom_emblem = emblem
        self.__ally_kingdoms = set()
        Kingdom.add_kingdom(self)
    
    @classmethod
    def get_kingdom(cls, name):
        if name in cls.__kingdoms.keys():
            return cls.__kingdoms[name]
        else:
            raise KingdomNotFound
    
    @classmethod
    def add_kingdom(cls, kingdom):
        cls.__kingdoms[kingdom.name()] = kingdom
    
    def get_allies(self):
        allies = []
        for kingdom in self.__ally_kingdoms:
            allies.append(kingdom.name())
        return allies
    
    def name(self):
        return self.__kingdom_name
    
    def emblem(self):
        return self.__kingdom_emblem

    def emblem_length(self):
        return len(self.emblem())
    
    def add_ally(self, otherKingdom):
        if otherKingdom.name() == None:
            raise KingdomNotFound
        elif otherKingdom == self:
            raise InvalidAllyKingdom("Cannot add itself as ally")
        else:
            if not self.is_ally(otherKingdom):
                self.__ally_kingdoms.add(otherKingdom)
                otherKingdom.add_ally(self)

    def is_ally(self, otherKingdom):
        return otherKingdom in self.__ally_kingdoms

    def total_allies(self):
        return len(self.__ally_kingdoms)

    def send_message(self, message):
        otherKingdom = message.get_receiver()
        if otherKingdom == self:
            raise InvalidMessageException("Cannot send message to itself")
        
        response = MessageVerify.verify(otherKingdom, message.get_message())
        
        if response:
            self.add_ally(otherKingdom)
        
        return response

    def is_ruler(self):
        return self.total_allies >= 3

    @classmethod
    def get_all(cls):
        for kingdom_name in cls.__kingdoms.keys():
            yield cls.__kingdoms[kingdom_name]
        
    @classmethod
    def get_ruler(cls):
        for kingdom in cls.get_all():
            if kingdom.total_allies() >= 3:
                return kingdom
        return None


    

