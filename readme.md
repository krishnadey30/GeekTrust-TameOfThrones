&copy; Copyright (c) 2020, Krishna Dey. All rights reserved.
# Geektrust Challenges
Challenges on Geektrust with readable, scalable and optimised code.

# Challenge 1: A Golden Crown

##### Problem context: 
Each kingdom has an animal emblem and Shan needs to send a message with the animal in the message to win them over.
SPACE emblem - Gorilla, LAND emblem - Panda, WATER emblem - Octopus, ICE emblem - Mammoth, AIR emblem - Owl, FIRE emblem - Dragon.

Your coding challenge is to have King Shan send secret message to each kingdom and win them over. Once he wins 3 more kingdoms, he is the ruler! The secret message needs to contain the letters of the animal in their emblem.
To make the secret message encrypted, King Shan uses a secret key, which is the number of characters in the emblem. If King Shan wants to send a message to kingdom Air, he uses the number 3 as the cipher key, as emblem ‘owl’ has 3 characters. So, to encrypt the letter ‘a’, just move 3 letters clockwise on the message wheel, which will give the letter ‘d’.

##### Solution steps:
	1.  Read the Kingdom Name and Message Sent.
	2.  Send Message to the respective Kingdom and wait for their reply.
	3.  If the reply is positive then add the Kingdom as an ally of Space kingdom.
	4.  Get the Ruling Kingdom at the end.


###  Running:

##### Installing Dependencies 
```bash
pip install -r requirements.txt
```

##### Executing Solution
```bash
python -m geektrust <abs_path_to_input_file>
```

##### Running Tests
All tests are in `tests_all_unit.py` file.
```bash
python tests_all_unit.py 
```
