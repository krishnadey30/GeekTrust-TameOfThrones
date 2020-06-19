from exceptions import KingdomNotFound, InvalidAllyKingdom, InvalidMessageException
from MessageVerify import MessageVerify

class Kingdom:
    __kingdoms = {}
    def init(self, name, emblem):
        self.__kingdom_name = name
        self.__kingdom_emblem = emblem
        self.__ally_kingdoms = set()
        __kingdoms[name] = self
    
    @staticmethod
    def get_kingdom(name):
        if name in __kingdoms.keys():
            return __kingdoms[name]
        else:
            raise KingdomNotFound
    
    def get_allies(self):
        return self.__ally_kingdoms
    
    def name(self):
        return self.__kingdom_name
    
    def emblem(self):
        return self.__kingdom_emblem

    def emlem_length(self):
        return len(self.emblem())
    
    def add_ally(self, otherKingdom):
        if otherKingdom.name() == None:
            raise KingdomNotFound
        elif otherKingdom == self:
            raise InvalidAllyKingdom("Cannot add itself as ally")
        else:
            if not is_ally(self, otherKingdom):
                self.__ally_kingdoms.add(otherKingdom)
                otherKingdom.add_ally(self)

    def is_ally(self, otherKingdom):
        return otherKingdom in self.__ally_kingdoms

    def total_allies(self):
        return len(self.__ally_kingdoms)

    def send_message(self, otherKingdom, message):
        if otherKingdom == self:
            raise InvalidMessageException("Cannot send message to itself")
        
        response = MessageVerify.verify(otherKingdom, message)
        
        if response:
            self.add_ally(otherKingdom)
        
        return response

    def is_ruler(self):
        return self.total_allies >= 3

    @staticmethod
    def get_all():
        for kingdom_name in __kingdoms.key():
            yield __kingdoms[kingdom_name]
        
    @staticmethod
    def get_ruler():
        for kingdom in get_all():
            if kingdom.total_allies() >= 3:
                return kingdom
        return None


    

