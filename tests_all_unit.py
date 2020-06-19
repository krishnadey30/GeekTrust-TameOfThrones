import unittest
from kingdom import Kingdom
from Message import Message
from MessageVerify import MessageVerify
class TestKingdom(unittest.TestCase):
    def test_init(self):
        name = "ICE"
        emblem = "MAMMOTH"
        ice_kingdom = Kingdom(name, emblem)
        self.assertNotEqual(None, ice_kingdom)
        Kingdom.remove_all_kingdoms()
    
    def test_name(self):
        name = "ICE"
        emblem = "MAMMOTH"
        ice_kingdom = Kingdom(name, emblem)
        self.assertEqual(name, ice_kingdom.name())
        Kingdom.remove_all_kingdoms()

    def test_emblem(self):
        name = "ICE"
        emblem = "MAMMOTH"
        ice_kingdom = Kingdom(name, emblem)
        self.assertEqual(emblem, ice_kingdom.emblem())
        Kingdom.remove_all_kingdoms()
    
    def test_emblem_length(self):
        name = "ICE"
        emblem = "MAMMOTH"
        ice_kingdom = Kingdom(name, emblem)
        self.assertEqual(len(emblem), ice_kingdom.emblem_length())
        Kingdom.remove_all_kingdoms()
    
    def test_get_kingdom(self):
        name = "ICE"
        emblem = "MAMMOTH"
        ice_kingdom = Kingdom(name, emblem)
        self.assertEqual(ice_kingdom, Kingdom.get_kingdom(name))
        Kingdom.remove_all_kingdoms()

    def test_add_ally_and_is_ally(self):
        name = ["ICE", "AIR", "WATER"]
        emblem = ["MAMMOTH", "OWL", "OCTOPUS"]
        ice_kingdom = Kingdom(name[0], emblem[0])
        air_kingdom = Kingdom(name[1], emblem[1])
        water_kingdom = Kingdom(name[2], emblem[2])
        ice_kingdom.add_ally(air_kingdom)
        self.assertTrue(ice_kingdom.is_ally(air_kingdom))
        self.assertTrue(air_kingdom.is_ally(ice_kingdom))
        self.assertFalse(water_kingdom.is_ally(ice_kingdom))
        Kingdom.remove_all_kingdoms()
    
    def test_ally_count(self):
        name = ["ICE", "AIR", "WATER"]
        emblem = ["MAMMOTH", "OWL", "OCTOPUS"]
        ice_kingdom = Kingdom(name[0], emblem[0])
        air_kingdom = Kingdom(name[1], emblem[1])
        water_kingdom = Kingdom(name[2], emblem[2])
        ice_kingdom.add_ally(air_kingdom)
        ice_kingdom.add_ally(water_kingdom)
        self.assertEqual(2, ice_kingdom.total_allies())
        self.assertEqual(1, water_kingdom.total_allies())
        self.assertNotEqual(2, air_kingdom.total_allies())
        Kingdom.remove_all_kingdoms()

    def test_send_message(self):
        name = ["ICE", "AIR"]
        emblem = ["MAMMOTH", "OWL"]
        ice_kingdom = Kingdom(name[0], emblem[0])
        air_kingdom = Kingdom(name[1], emblem[1])
        message_text = "ROZO"
        message = Message(air_kingdom, ice_kingdom, message_text)
        response = air_kingdom.send_message(message)
        self.assertFalse(response)
        message = Message(ice_kingdom, air_kingdom, message_text)
        response = ice_kingdom.send_message(message)
        self.assertTrue(response)
        Kingdom.remove_all_kingdoms()

    def test_check_ruler(self):
        name = ["ICE", "AIR", "WATER", "FIRE"]
        emblem = ["MAMMOTH", "OWL", "OCTOPUS", "DRAGON"]
        ice_kingdom = Kingdom(name[0], emblem[0])
        air_kingdom = Kingdom(name[1], emblem[1])
        water_kingdom = Kingdom(name[2], emblem[2])
        fire_kingdom = Kingdom(name[3], emblem[3])
        ice_kingdom.add_ally(air_kingdom)
        ice_kingdom.add_ally(water_kingdom)
        ice_kingdom.add_ally(air_kingdom)
        ice_kingdom.add_ally(fire_kingdom)
        self.assertTrue(ice_kingdom.is_ruler())
        self.assertFalse(fire_kingdom.is_ruler())
        Kingdom.remove_all_kingdoms()

    def test_get_ruler(self):
        name = ["ICE", "AIR", "WATER", "FIRE"]
        emblem = ["MAMMOTH", "OWL", "OCTOPUS", "DRAGON"]
        ice_kingdom = Kingdom(name[0], emblem[0])
        air_kingdom = Kingdom(name[1], emblem[1])
        water_kingdom = Kingdom(name[2], emblem[2])
        fire_kingdom = Kingdom(name[3], emblem[3])
        ice_kingdom.add_ally(air_kingdom)
        ice_kingdom.add_ally(water_kingdom)
        ice_kingdom.add_ally(air_kingdom)
        ice_kingdom.add_ally(fire_kingdom)
        self.assertEqual(ice_kingdom, Kingdom.get_ruler())
        self.assertNotEqual(fire_kingdom, Kingdom.get_ruler())
        Kingdom.remove_all_kingdoms()

class TestMessage(unittest.TestCase):
    def test_get_sender(self):
        name = ["ICE", "AIR"]
        emblem = ["MAMMOTH", "OWL"]
        ice_kingdom = Kingdom(name[0], emblem[0])
        air_kingdom = Kingdom(name[1], emblem[1])
        message_text = "ROZO"
        message = Message(air_kingdom, ice_kingdom, message_text)
        self.assertEqual(message.get_sender(), air_kingdom)
        self.assertNotEqual(message.get_sender(), ice_kingdom)
        Kingdom.remove_all_kingdoms()
    
    def test_get_receiver(self):
        name = ["ICE", "AIR"]
        emblem = ["MAMMOTH", "OWL"]
        ice_kingdom = Kingdom(name[0], emblem[0])
        air_kingdom = Kingdom(name[1], emblem[1])
        message_text = "ROZO"
        message = Message(air_kingdom, ice_kingdom, message_text)
        self.assertEqual(message.get_receiver(), ice_kingdom)
        self.assertNotEqual(message.get_receiver(), air_kingdom)
        Kingdom.remove_all_kingdoms()
    
    def test_get_message(self):
        name = ["ICE", "AIR"]
        emblem = ["MAMMOTH", "OWL"]
        ice_kingdom = Kingdom(name[0], emblem[0])
        air_kingdom = Kingdom(name[1], emblem[1])
        message_text = "ROZO"
        message = Message(air_kingdom, ice_kingdom, message_text)
        self.assertEqual(message.get_message(), message_text)
        Kingdom.remove_all_kingdoms()

class TestMessageVerify(unittest.TestCase):
    def test_verify(self):
        name = "AIR"
        emblem = "OWL"
        air_kingdom = Kingdom(name, emblem)
        message_text = "ROZO"
        response = MessageVerify.verify(air_kingdom, message_text)
        self.assertTrue(response)
        message_text = "OWLAOWLBOWLC"
        response = MessageVerify.verify(air_kingdom, message_text)
        self.assertFalse(response)
        Kingdom.remove_all_kingdoms()

if __name__ == '__main__':
    unittest.main()