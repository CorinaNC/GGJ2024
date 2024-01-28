label splashscreen:
    scene black
    with Pause(1)

    show mcfc at truecenter with dissolve
    with Pause(2)

    hide mcfc with dissolve
    with Pause(2)
    
    return

label scene1Intro:
    scene black
    centered "{cps=20}> Day 1.{/cps}"  
    pause(1)
    jump scene1_1

label scene1_1:

    play sound phoneVibrate

    n.c "Bzzzt.. Bzzt."

    n.c "There was an annoying ringing in my ear."

    play sound phoneVibrate

    n.c "Bzzt.. Bzzt…" 

    n.c "It was really damn annoying."

    play sound phoneVibrate

    n.c "..."

    Me.c "Can someone please turn that alarm off?"

    Me.c "My back is killing me, I don’t need the alarm damaging my hearing to accompany it."

    Eve.c "Heh, that’s your own fault for hunching all night, Zy."

    scene dormRoom # dormroom goes here
    with fade

    show Eve smirk
    with dissolve

    play music t_eve fadein 2 fadeout 2 #eve ost goes here

    n.c "Didn’t I tell her to stop calling me that? "
    
    n.c "It’s a little awkward now that we actually know each other.. "
    
    n.c "Especially since we’re going to be roommates for the next year."

    Me.c "I thought I told you to stop calling me that." 

    n.c "I felt my face deadpan as the words left my mouth."

    show Eve neutral

    Eve.c "Hey, it’s just habit."

    show Eve smirk

    Eve.c "How am I supposed to see you as anything other than your edgy middle school syndrome username?"

    show Eve laugh
    
    n.c "She stuck her tongue out, a motion that I physically cringed at."

    Me.c "It’s just a normal username…"

    Me.c "And you’re acting as if you’re not equally as ‘edgy’."

    show Eve frown

    Eve.c "‘Aldebran’ is not edgy."

    Eve.c "..."

    show Eve laugh

    Eve.c "Not as edgy as ‘Zylothh’."

    Me.c "..whatever you want to believe, Eve."

    show Eve smirk

    Eve.c "L.O.L that rhymed."

    n.c "Shaking my head as a nonverbal response, I took a look at the alarm clock that had since muted its ringing."

    Me.c "Eve, hey."

    show Eve confused

    n.c "She turns her head towards me as I gestured to the alarm clock."

    Me.c "We should probably go to class, it’s the first day, you know?"

    show Eve neutral

    Eve.c "Man, are you going to be one of those brown nosers who are super anal about attendance?"

    Eve.c "‘cause if so, then I don’t know you at all!  Your majesty-of-Procrastination."

    Me.c "Damn, who do you take me for?  I didn’t even attend my classes back at my old University."

    n.c "I wasn’t expecting anything to change from when I lived in my hometown.  The fact that I was even here was sort of a miracle."

    play sound shuffling

    Me.c "I mean, I checked the ReviewMyInstructors for our first class.  He has really high ratings."

    show Eve confused
    
    Eve.c "What do those chumps know?"

    show Eve neutral
    
    Eve.c "Last time I followed what was on ReviewMyInstructors, I got hit with a no-curve test-heavy grading scale."

    Eve.c "The site’s moderation is doodoo and there’s no way to filter who actually knows what they’re talking about."

    Me.c "My experiences with it have been fine, maybe it’s your problem."

    Eve.c "Maybe it is.."

    Eve.c "..."

    show Eve frown

    Eve.c "No, definitely not, I’m perfect and the best person ever."

    Eve.c "All my opinions are verified, blue checkmark and all."

    jump scene1_2
