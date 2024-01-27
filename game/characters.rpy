# characters are defined here

init python:
    class Char:
        def __init__(self, character, name, affection=None):
            self.c = character
            self.name = name
            self.affection = affection
            

define Cam = Char(Character("[povname]", color="#993300"), "[povname]")
define Student = Char(Character("Student A", color="#000037"), "Student A", 0)
define Bill = Char(Character("William 'Bill' Ceriph", color="ffc000"), "Bill", 0)
define Eve = Char(Character("Eve", color="#c719f8"), "Eve", 0)
define Prof = Char(Character("Professor Muskerburg", color="#b1ff00"), "Professor Muskerburg", 0)

# Character sprites defined here

image Cam neutral = "green normal.png"

# backgrounds defined here

# choice variables defined here

$ pineapple = None
