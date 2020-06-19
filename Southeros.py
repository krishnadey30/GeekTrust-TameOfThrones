from kingdom import Kingdom
class Southeros:

    def __init__(self):
        self.__rulingKingdom = None

    def __init__(self, kingdoms):
        self.__rulingKingdom = None
        self.register_kingdoms(kingdoms)

    def __register_kingdom(self, name, emblem):
        new_kingdom = Kingdom(name, emblem)
        return new_kingdom
    
    def register_kingdoms(self, kingdoms):
        for name, emblem in kingdoms:
            self.__register_kingdom(name, emblem)
    
    def get_kingdom(self, name):
        return Kingdom.get_kingdom(name)

    def ruler(self):
        if self.__rulingKingdom == None:
            self.__rulingKingdom = self.__ruling_kingdom()
        return self.__rulingKingdom

    def __ruling_kingdom(self):
        return Kingdom.get_ruler()

