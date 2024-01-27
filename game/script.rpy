# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Corina = Character(_("Corina"), color="#c8c8ff")

default cool = False


# The game starts here.

label start:
    play music "illurock.opus"

    scene bg lecturehall
    with fade

    Corina "Hi cuties! Welcome to my world"

    return
