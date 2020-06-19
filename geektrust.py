from Southeros import Southeros
from Message import Message
import sys
def register_all_kingdoms():
    kingdoms = [("SPACE","GORILLA"), ("LAND","PANDA"),("WATER","OCTOPUS"),
        ("ICE", "MAMMOTH"), ("AIR", "OWL"), ("FIRE", "DRAGON")]
    southeros = Southeros(kingdoms)
    return southeros

def get_kingdom_and_message(text):
    splitted_text = text.split()
    kingdom_name = splitted_text[0]
    ciphered_text = ""
    for c in splitted_text[1:]:
        ciphered_text += c
    return kingdom_name, ciphered_text

def main():
    southeros = register_all_kingdoms()
    space_kingdom = southeros.get_kingdom("SPACE")
    input_file = sys.argv[1]
    # parse the file and process the command
    with open(input_file) as fp: 
        Lines = fp.readlines() 
        for line in Lines:
            kingdom_name, ciphered_text = get_kingdom_and_message(line)
            kingdom = southeros.get_kingdom(kingdom_name)
            message = Message(space_kingdom, kingdom, ciphered_text)
            space_kingdom.send_message(message)
    # print the output
    ruler = southeros.ruler()
    if ruler is None:
        print("NONE")
    else:
        print(ruler.name(), end = " ")
        for kingdom_name in ruler.get_allies():
            print(kingdom_name, end = " ")
        print()

if __name__ == "__main__":
    main()