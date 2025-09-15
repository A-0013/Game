 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define m = Character("MC")
define r = Character("Reina")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene fast_food entrance
    with fade

    m "Hmm is this the right place?"

    m "I'll ask the girl standing there."

    m "Uh hey is this the humble sandwich shop?"
 
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Reina normal:
        zoom 0.25 xalign 0.5 yalign 2.0
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

    # First Dialogue Branch
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

    # Game continues after choice
    label inside:
        
        scene fast_food_interior_day
        with fade

        r "Here we have the inside of the beatiful humble sandwich shop!"
        
        show Reina smile:
            zoom 0.25 xalign 0.5 yalign 2.0
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

        r "We'll start by making a basic PB&J"

        r "Use you mouse to drag and drop the items in the correct order"


    # This ends the game.

    return
