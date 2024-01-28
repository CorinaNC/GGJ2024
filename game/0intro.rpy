define povname = ''
define fifthFaveColor = ''

label start:    

    scene black
    with flash
    play music ambience

    centered "> Work In Progress presents itself as an experience, both in name and meaning."  
    centered "> The endless timeline that makes up being human holds shelter to an infinite amount of stories."  
    centered "> Our tragedies, our comedies, the mundane and the epic; no matter how they are divided or labeled,"
    centered "> they are all equally unimportant."
    centered "> And yet, this is the one that you decided to select."
    centered "> I’m not a huge fan of prefaces,"
    centered "> So how about we minimize the amount of reading."
    centered '> ...'
    centered '> ...'
    centered '> Just kidding!'
    centered '> This is a visual {b}novel{/b} after all.'
    centered '> Definitions are all that exist for bringing meaning to our consonance.'
    centered '> Now tell me a bit about you.'
    
    python:
        while povname == '':
            povname = renpy.input("> What is your nickname?", screen='inputCenter', allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", length=10)
            povname = povname.strip()
        
    centered "> If you had to choose between {b}pineapple on pizza{/b} or a {b}pineapple full of pizza{/b}, which would you choose?"
    
    menu:
        "Pineapple on pizza":
            $ pineapple = True
        "A pineapple full of pizza":
            $ pineapple = False

    centered "> What is your fifth favorite color of {color=#f00}ROYGBIV{/color}?" 

    python:
        while fifthFaveColor == '':
            fifthFaveColor = renpy.input("Type in a letter (ROYGBIV)", screen='inputCenter', allow="ROYGBIVroygbiv", length=1)
            fifthFaveColor = fifthFaveColor.upper()

    centered "> ..."
    centered "> {cps=20}Alright, that's enough out of you.{/cps}"
    centered "> {cps=20}That's all that we needed, for now.{/cps}"
    centered "> {cps=20}Until we meet {b}again.{/b}{/cps}"
    
    jump scene1Intro