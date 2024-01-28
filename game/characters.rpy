# characters are defined here

init python:
    class Char:
        def __init__(self, character, name, affection=None):
            self.c = character
            self.name = name
            self.affection = affection
            
define n = Character(None, what_italic=True)
define Me = Char(Character("Me", color="#993300"), "Me")
define Student = Char(Character("Student A", color="#000037"), "Student A", 0)
define Bill = Char(Character("William 'Bill' Ceriph", color="ffc000"), "Bill", 0)
define Eve = Char(Character("Eve", color="#c719f8"), "Eve", 0)
define Prof = Char(Character("Professor Muskerburg", color="#b1ff00"), "Professor Muskerburg", 0)

# Character sprites defined here

#Cam

image Cam neutral = "green normal.png"

#Eve

image Eve neutral:
    "images/char/eve/eve.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15


#Bill



#Prof


# backgrounds defined here

# choice variables defined here

$ pineapple = None