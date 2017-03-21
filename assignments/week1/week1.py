"""

Samuel Cuthbertson

sacu2067

samuel.cuthbertson@colorado.edu

Week 1

"""
from random import random

for x in range(0,3):

    current = "I";
    for x in range(0,100):
        print(current, end="")
        rand = random();
        nextchar = ""

        if current == "I":
            nextchar = "_"
        elif current == "_":
            if rand <= .5:
                nextchar = "a"
            else:
                nextchar = "l"
        elif current == "a":
            if rand <= .4:
                nextchar = "m"
            else:
                nextchar = "l"
        elif current == "m":
            if rand <= .8:
                nextchar = "_"
            else:
                nextchar = "!"
        elif current == "l":
            nextchar = "i"
        elif current == "i":
            if rand <= .95:
                nextchar = "v"
            else:
                nextchar = "n"
        elif current == "v":
            nextchar = "e"
        elif current == "n":
            nextchar = "e"
        elif current == "e":
            nextchar = "!"
        elif current == "!":
            if rand <= .7:
                nextchar = "_"
            elif rand <= .9:
                nextchar = "I"
            else:
                nextchar = "!"
        current = nextchar
    print()
