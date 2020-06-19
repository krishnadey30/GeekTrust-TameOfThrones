from Southeros import Southeros
from Message import Message
import sys

"""Registers all the Kingdoms of Southeros"""
def register_all_kingdoms():
    kingdoms = [("SPACE","GORILLA"), ("LAND","PANDA"),("WATER","OCTOPUS"),
        ("ICE", "MAMMOTH"), ("AIR", "OWL"), ("FIRE", "DRAGON")]
    southeros = Southeros(kingdoms)
    return southeros

"""Splits the given text to two parts using first space, first part being the kingdom name 
and second part being the text message sent to the kingdom
"""
def get_kingdom_and_message(text):
    splitted_text = text.split()
    kingdom_name = splitted_text[0]
    ciphered_text = ""
    for c in splitted_text[1:]:
        ciphered_text += c
    return kingdom_name, ciphered_text

"""main function of the Tame of Thrones""""
def main():
    southeros = register_all_kingdoms()    # registers all the kindoms of Southeros
    space_kingdom = southeros.get_kingdom("SPACE")    # gets the space kingdom object
    input_file = sys.argv[1]    # file location
    
    # parse the file and process the command
    with open(input_file) as fp: 
        Lines = fp.readlines() 
        for line in Lines:
            kingdom_name, ciphered_text = get_kingdom_and_message(line)    # retrieving kingdom name and message
            kingdom = southeros.get_kingdom(kingdom_name)    # gets the kingdom to which message should be sent
            message = Message(space_kingdom, kingdom, ciphered_text)    # Creates the message
            space_kingdom.send_message(message)    # sends the message
    
    # print the output
    ruler = southeros.ruler()   # get the ruler of Southeros
    if ruler is None:
        print("NONE")    # no ruler got majority
    else:
        print(ruler.name(), end = " ")    # found a majority ruler
        for kingdom_name in ruler.get_allies():    # found it's allies
            print(kingdom_name, end = " ")
        print()

if __name__ == "__main__":
    main()