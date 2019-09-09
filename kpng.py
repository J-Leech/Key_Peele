"""Key & Peele college name generator"""

import sys
import random

print('Welcome to the Key & Peele East/West College Bowl name generator!')
print("Let's see who's in the line up today:")

FIRST = ("D'Marcus", 'T.J.', "T'Varisuness", 'Tyroil', "D'Squarius", 'Ibrahim', "D'Jasper",
         'Leoz Maxwell', 'Javarius Jamar Javarison', 'Davion', 'Hingle', "L'Carpetron",
         "J'Drinkalage", 'Xmus Jaxon Flaxon', 'Saggitariutt', "D'Glester", 'Swirvithan',
         'Quatro', 'Ozmataz', 'Beezer Twelve', 'Shakiraquan T.G.I.F.', 'X-Wing',
         'Sequester', 'Scoish Velociraptor', 'T.J A.J. R.J.', 'Eeeeeeeee', 'Donkey',
         'Torque', 'The Player Formerly Known as')

LAST = ('Williums', 'Juckson', 'King', 'Smoochie-Wallace', 'Green Jr.', 'Moizoos',
        'Tacktheritrix', 'T. Billings-Clyde', 'Probincrux III', 'Jilliumz', 'Lamar',
        'Shower-Handel', 'McCringleberrry', 'Dookmarriot', 'Morgoone', 'Flaxon-Waxon',
        'Jefferspin', 'Hardunkichud', "l'Goodling-Splatt", 'Quatro', 'Buckshank',
        'Washingbeard', 'Carter', '@Aliciousness', 'Grundelplith M.D.', 'Maloish',
        'Backslashinforth V', 'Eeeeeeeeee', 'Teeth', 'Lewith', 'Mousecop')

while True:
    FIRST_NAME = random.choice(FIRST)
    LAST_NAME = random.choice(LAST)
    print("\n\n")
    print("{} {}".format(FIRST_NAME, LAST_NAME), file=sys.stderr)
    print("\n\n")

    NEXT_UP = input("\n\nSee who's next up?(Press Enter or n to exit)\n")
    if NEXT_UP.lower() == "n":
        break

    input("\nReady?")
