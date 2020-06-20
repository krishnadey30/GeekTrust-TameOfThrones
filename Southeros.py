from kingdom import Kingdom
class Southeros:
    """Class to contain the World of Southeros"""

    def __init__(self, kingdoms=[]):
        """
        Args:
            kingdoms (list of tuple of str,str): List of Kingdoms and their emblems, 
                defaults to empty List
        """
        self.__rulingKingdom = None
        self.__kingdom_count = 0
        self.register_kingdoms(kingdoms)

    def register_kingdom(self, name, emblem):
        """Creates a Kingdom Class for the given kingdom name and emblem
        Args:
            name (string): Name of the Kingdom
            emblem (string): Emblem of the Kingdom

        Returns:
            Kingdom Object: Return the new kingdom object 
        """
        new_kingdom = Kingdom(name, emblem)
        self.__kingdom_count += 1
        return new_kingdom
    
    def register_kingdoms(self, kingdoms):
        """Registers all the kingdoms
        Args:
            kingdoms (list of tuple of str,str): List of Kingdoms and their emblems
        """
        for name, emblem in kingdoms:
            self.register_kingdom(name, emblem)
    
    def get_kingdom(self, name):
        """Get the Kingdom Object from the Name of the kingdom
        Args:
            name (string): Name of the Kingdom

        Returns:
            Kingdom Object: Kingdom Object for the given name

        Raises:
            KingdomNotFound:
                If no Kingdom is found for the kingdom name passed in as a parameter.
        """
        return Kingdom.get_kingdom(name)

    def ruler(self):
        """Get the Ruler of Southeros
        Returns:
            Kingdom Object: Ruling Kingdom Object otherwise None
        """
        if self.__rulingKingdom == None:
            self.__rulingKingdom = self.__ruling_kingdom()
        return self.__rulingKingdom

    def __ruling_kingdom(self):
        """Get the Ruler of Southeros
        Returns:
            Kingdom Object: Ruling Kingdom Object otherwise None
        """
        return Kingdom.get_ruler()

    def get_total_kingdoms(self):
        """Return the count of Total Kingdoms in Southeros
        Returns:
            int: Total count of Kingdoms
        """
        return self.__kingdom_count