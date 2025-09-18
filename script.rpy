# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("MC")
define r = Character("Reina")
define b = Character("???")
define d = Character("Don")

default pb_spawned = False
default jam_spawned = False
default has_won = False
default placed_parts = []
default tutorial_completed = False

# The game starts here.
label start:
    #make a 'set' of sandwhich pieces (when all the pieces of the set are together its a win)
    $ placed_parts = []
    #set has won to false so that way repeat play thrus possible
    $ has_won = False
    $ tutorial_completed = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene fast_food_entrance
    with fade

    m "Hmm is this the right place?"

    m "I'll ask the girl standing there."

    m "Uh hey is this the humble sandwich shop?"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Reina normal:
        zoom 0.25 xalign 0.5 yalign 1.0
    with dissolve

    # These display lines of dialogue.

    r "Huh?"

    r "Oh, you must be the new recruit."

    m "Uh yeah."

    show Reina smile

    r "Welcome to the humble sandwich shop, I'm Reina"

    show Reina laugh

    r "I look forward to working with you!"

    m "Same here"

    show Reina smile

    r "Since you're here already so early, I can be the one to show you around today."

    r "Sooooo, do you think you have what it takes to makes sandwiches here?"

    ### First Dialogue Branch ###
    menu:

        "I think so.":

            jump yes

        "I've never made a sandwich in my entire life. Please Help.":

            jump no

label yes:

    show Reina laugh

    r "Awesome. I'm sure you'll do just fine here at the humble sandwich shop!"

    m "Damn right!"

    jump inside


label no:

    show Reina wink

    r "Oh really? I've been wanting to teach a newbie."

    r "Ok that settles it. After I show around, I show you how we make our sandwiches here."

    r "Don't worry I know you'll do great!"

    m "Ok"

    "Damn I was hoping I could get someone else to teach me."

    jump inside

    #### Game continues after choice ###
    label inside:

        scene fast_food_interior_day
        with fade

        r "Here we have the inside of the beatiful humble sandwich shop!"

        show Reina smile:
            zoom 0.25 xalign 0.5 yalign 1.0
        with dissolve

        r "Pretty cool huh?"

        m "It's pretty neat I guess."

        r "So you're new to the art of sandwich making huh?"

        m "Apparently..."

        show Reina wink

        r "Well it's a good thing you ran into me first. I'll have you know I'm best the sandwich builder in the shop."

        r "No one can do it better than me. I'll be happy to show you the ropes."

        show Reina laugh

        r "Ok lets get to sandwich making!"

        r "We'll start by making a basic PB&J and BLT!"

        "You could speak at a normal volume y'know..."

        show Reina smile

        r "Pay attention now. Game mechanics are coming in hot!"

        r "Use you mouse to drag and drop the items in the correct order"

        show Reina laugh

        r "It's as simple as that!"

        ############ Post-Tutorial #############

        # Call the tutorial first
        call screen sandwich_tutorial

        # After tutorial, show the actual game
        scene fast_food_interior_day
        with fade

        show Reina smile:
            zoom 0.25 xalign 0.75 yalign 1.0
        with dissolve

        r "Wow, you built those sandwiches with conviction!"

        r "I just know you'll do great here."

        b "Never cease to show up super early, huh Reina?"

        show Boss normal:
            xalign 0.25 yalign 0.35
        with dissolve

        show Reina laugh

        r "Hehe you know me, I just can't get enough of this place!"

        show Reina smile

        r "By the way, the new hire got here early too. I was showing them how it's done."


        # Second Dialogue Branch

        menu:

            "Wait, is this guy the boss?":

                jump respect

            "Hey Reina, who's this old guy?":

                jump disrespect


    label respect:

        show Reina wink

        r "Yup, this is Don. He's the guy who built this place from the ground up."

        d "Good to meet you kid."

        d "I've been in this business for a while and while some may say I'm getting old..."

        d "I prefer the term, experienced."

        jump continue

    label disrespect:

        show Reina normal

        r "Newbie, that was definitely a question you just asked."

        show Reina smile

        r "This is Don. He's the boss here and he built this place from the ground up."

        d "Heh, old is one thing kid, but I prefer the term..."

        d "Experienced."

        jump continue



    label continue:

        show Reina smile

        d "So, seems like Reina taught you all the basics."

        d "Here's a word of advice kid."

        d "Never underestimate customers and their orders."

        "Heh, of course I know that. Sooner or later, I'll be the one telling new hires that."

        d "Ok, we should be opening soon."

        show Reina laugh

        r "Yes, time for your first day to truly begin newbie!"

        r "Good luck!"


        # End of first day after first level

        scene fast_food_entrance_day
        with fade

        show Reina smile:
            zoom 0.25 xalign 0.5 yalign 1.0
        with dissolve

        r "Good work today newbie, you didn't do half bad."

        show Reina laugh

        r "It'll only get better, I just know it!"

        show Reina smile

        r "Well see tomorrow newbie."


    # This ends the game.

    return

init python:
    # Safe drop handler that accepts either a single Drag object or a list/tuple of them.
    def place_ingredient(drop_target, drags):
        # drags may be a single Drag or a list/tuple of Drag
        if isinstance(drags, (list, tuple)):
            dragged = drags[0] if drags else None
        else:
            dragged = drags

        if dragged is None:
            return

        drag_name = getattr(dragged, "drag_name", None)
        if drag_name is None:
            return

        # Only accept drops on the plate
        if getattr(drop_target, "drag_name", "") == "plate":
            if drag_name not in placed_parts:
                placed_parts.append(drag_name)

            # Win check
            needed = {"lower_bread", "peanutbutter", "jelly", "topmost_bread"}
            if needed.issubset(set(placed_parts)):
                store.has_won = True
                renpy.restart_interaction()

    # helper to reset the mini-game
    def reset_sandwich():
        placed_parts[:] = []
        store.pb_spawned = False
        store.jam_spawned = False
        store.has_won = False