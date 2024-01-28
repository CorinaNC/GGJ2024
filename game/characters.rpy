# characters are defined here

init python:
    class Char:
        def __init__(self, character, name, affection=None):
            self.c = character
            self.name = name
            self.affection = affection
            
define n = Char(Character(None, what_italic=True), [povname])
define Me = Char(Character("Me", color="#009991"), "Cam")
define Student = Char(Character("Melonie", color="#e41b97"), "Melonie", 0)
define Bill = Char(Character("William 'Bill' Ceriph", color="ffc000"), "Bill", 0)
define Eve = Char(Character("Eve", color="#c719f8"), "Eve", 0)
define Prof = Char(Character("Professor Muskerburg", color="#b1ff00"), "Professor Muskerburg", 0)

# Character sprites defined here

#Cam

image Cam neutral:
    "images/assets/mcfc.png"
    
#Eve

image Eve neutral:
    "images/char/eve/eve.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15

image Eve laugh:
    "images/char/eve/Eve2.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15

image Eve smirk:
    "images/char/eve/Eve3.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15

image Eve frown:
    "images/char/eve/Eve4.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15

image Eve confused:
    "images/char/eve/Eve5.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15


image Eve playful:
    "images/char/eve/Eve6.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15

#Bill

image Bill neutral:
    "images/char/bill/Bill2.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.0

image Bill laugh:
    "images/char/bill/Bill4.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.0

image Bill smirk:
    "images/char/bill/Bill.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.0

image Bill demean:
    "images/char/bill/Bill3.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.0

#Prof

image Prof neutral:
    "images/char/muskerburg/Muskerberg1.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15

image Prof manic:
    "images/char/muskerburg/Muskerberg2.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15

image Prof smile:
    "images/char/muskerburg/Muskerberg3.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15


# blue people

image Student neutral:
    "images/char/npcs/melontits.png"
    zoom 0.4
    yanchor 0.0
    ypos 0.15

# backgrounds defined here

# assets defined here

image mcfc:
    "images/assets/mcfc.png"

# choice variables defined here

define realName = '{b}{color=#FFD700}Cam{/color}{/b}'
$ pineapple = None