class MessageVerify:
    @staticmethod
    def verify(prospect_kingdom, message):
        message_dict = get_frequency_of_each_character(message)
        emblem_dict = get_frequency_of_each_character(prospect_kingdom.emblem())
        for key in emblem_dict.keys():
            message_key_count = message_dict.get(key, 0)
            if message_key_count < emblem_dict[key]: return False
        return True

    @staticmethod
    def get_frequency_of_each_character(text):
        freq = {}
        for key in text: 
            res[key] = freq.get(key, 0) + 1
        return freq