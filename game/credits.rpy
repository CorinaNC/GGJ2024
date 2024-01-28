init:
    $ flash = Fade(.25, 0, .75, color="#ffffff")

label credits:
    play sound flash
    play music ambience
    with fade
    scene black
    with flash
    
    centered "> {cps=15}{color=#FF0000}And that's the end of the demo.{/color}{/cps}"
    centered "> {cps=15}{color=#FF0000}Thank you for reading.{/color}{/cps}"
    centered "> {cps=15}{color=#FF0000}Made for Global Game Jam 2024.{/color}{/cps}"

    show text "{cps=15}> Credits{/cps}" with dissolve

    $ renpy.pause(2.0)

    show text "Written & Directed by\n\nCorina Conklin" with dissolve

    $ renpy.pause(5.0)

    show text "Spritework, CGs, and Character Designs \n\nAllison Lee" with dissolve

    $ renpy.pause(5.0)

    show text "Music and Design \n\nManan Chaturvedi" with dissolve

    $ renpy.pause(5.0)

    show text "Backgrounds \n\nKhanhLoan Lambuu" with dissolve

    $ renpy.pause(5.0)

    show text "Sound Effects & Additional Music by\n\nPixabay" with dissolve

    $ renpy.pause(5.0)