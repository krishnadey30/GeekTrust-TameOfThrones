class MessageVerify:
    @classmethod
    def verify(cls, prospect_kingdom, message):
        message_dict = cls.get_frequency_of_each_character(message)
        chiper_emblem_name = cls.chiper_emblem(prospect_kingdom.emblem(), 
                prospect_kingdom.emblem_length())
        emblem_dict = cls.get_frequency_of_each_character(chiper_emblem_name)
        for key in emblem_dict.keys():
            message_key_count = message_dict.get(key, 0)
            if message_key_count < emblem_dict[key]: return False
        return True

    @classmethod
    def get_frequency_of_each_character(cls, text):
        freq = {}
        for key in text: 
            freq[key] = freq.get(key, 0) + 1
        return freq

    @classmethod
    def chiper_emblem(cls, text, chiper_key):
        chiper_word = ""
        for char in text:
            if char >= 'A' and char <= 'Z':
                newChar = chr(((ord(char) - 65 + chiper_key)%26)+65)
                chiper_word += newChar
            else:
                chiper_word += char
        return chiper_word