# Declare characters used by this game.



# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene lecturehall
    with fade
    
    "Welcome to this weird untitled visual novel"
    
    scene bg uni
    with fade
    
    

    python:
        povname = renpy.input("What is your name?", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=10)
        povname = povname.strip()

        if not povname:
            povname = "Cam"

    
    
    Cam.c "My name is [povname], and today is.."

    Bill.c "That's [Bill.c] to you."

    show green normal
    with dissolve

    
    return
