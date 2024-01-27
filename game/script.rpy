# Declare characters used by this game.


# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.

define povname = ''
define fifthFaveColor = ''

label splashscreen:
    scene BLACK
    with Pause(1)

    show mcfc at truecenter with dissolve
    with Pause(1)

    hide mcfc with dissolve
    with Pause(1)

    show text "Work In Progress" with dissolve
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    return

# The game starts here.
label start:
    
    centered "Work In Progress presents itself as an experience, both in name and meaning."  
    centered "The endless timeline that makes up being human holds shelter to an infinite amount of stories."  
    centered "Our tragedies, our comedies, the mundane and the epic; no matter how they are divided or labeled,"
    centered "they are all equally unimportant."
    centered "And yet, this is the one that you decided to select."
    centered "I’m not a huge fan of prefaces, so how about we minimize the amount of reading in this visual novel…"
    centered '...'
    centered 'Just kidding, what did you think was going to happen?'
    centered 'Now tell me a bit about you.'
    
    python:
        while povname == '':
            povname = renpy.input("> What is your name?", screen='inputCenter', allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=10)
            povname = povname.strip()
        
    centered "> If you had to choose between pineapple on pizza or a pineapple full of pizza, which would you choose?"
    
    menu:
        "Pineapple on pizza":
            $ pineapple = True
        "A pineapple full of pizza":
            $ pineapple = False

    centered "> What is your fifth favorite color of ROYGBIV?" 

    python:
        while fifthFaveColor == '':
            fifthFaveColor = renpy.input("Type in a letter (ROYGBIV)", screen='inputCenter', allow="ROYGBIVroygbiv", length=1)
            fifthFaveColor = fifthFaveColor.upper()

    centered "..."
    centered "{cps=10}Alright, that's enough out of you.{/cps}"
    centered "{cps=10}That's all that we needed, for now.{/cps}"
    centered "{cps=10}Until we meet {b}again.{/b}{/cps}"

    with Pause(1)
    play music t_bill

    scene lecturehall
    with fade
    
    "Welcome to this weird untitled visual novel"

    Cam.c "My name is [povname], and today is.."

    Bill.c "That's [Bill.c] to you."

    show green normal
    with dissolve

    Cam.c "What's up"

    
    return
