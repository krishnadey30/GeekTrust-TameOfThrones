class MessageVerify:
    """Class that verifies if the message sent results in positive or negitive reply"""
    @classmethod
    def verify(cls, prospect_kingdom, message):
        """
        Args:
            prospect_kingdom (Kingdom Object): Reciever Kingdom
            message (string): message text that is sent
        Returns:
            bool: True if the condition is fullfilled, False otherwise
        """
        message_dict = cls.__get_frequency_of_each_character(message)
        chiper_emblem_name = cls.__chiper_emblem(prospect_kingdom.emblem(), 
                prospect_kingdom.emblem_length())
        emblem_dict = cls.__get_frequency_of_each_character(chiper_emblem_name)
        for key in emblem_dict.keys():
            message_key_count = message_dict.get(key, 0)
            if message_key_count < emblem_dict[key]: return False
        return True

    @classmethod
    def __get_frequency_of_each_character(cls, text):
        """Returns the frequency of each character in the given string"""
        freq = {}
        for key in text: 
            freq[key] = freq.get(key, 0) + 1
        return freq

    @classmethod
    def __chiper_emblem(cls, text, chiper_key):
        """Chiper the emblem text based on the length of the emblem"""
        chiper_word = ""
        for char in text:
            if char >= 'A' and char <= 'Z':
                newChar = chr(((ord(char) - 65 + chiper_key)%26)+65)
                chiper_word += newChar
            else:
                chiper_word += char
        return chiper_word