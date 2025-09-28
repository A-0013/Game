# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# callback function
init python:
    
    # audio channels
    renpy.music.register_channel("LoNoise","bgm") # BGM that loops 
    renpy.music.register_channel("trans1", "bgs", loop=False) # Transition (does not loop)
    renpy.music.register_channel("beep1", "sfx", loop=False) # Dialogue sfx (does not loop) 

    import math

    # This function makes continuous text sounds when characters speak
    def text_sounds(event, interact=True, **kwargs):
        if event == "show": # If textbox is shown
            what = renpy.store._last_say_what # Grabs the text that was most recently spoken on-screen
            if what:
                sound_count = len(what)
                
            else:
                sound_count = 5
            for _ in range(sound_count):
                randosound = renpy.random.randint(1, 11)
                renpy.sound.queue(f"audio/pack1/DialogueSFX/bleep026.ogg", channel="beep1", loop=False)
        elif event == "end" or event == "slow_done": # If there is a pause in the dialogue or the text has finished displaying
            renpy.sound.stop(channel="beep1")



#Character definitions using what callback
define m = Character("MC", callback=text_sounds)
define r = Character("Reina", callback=text_sounds)
define b = Character("???", callback=text_sounds)
define d = Character("Don", callback=text_sounds)


# The game starts here.

label start:

    pause 1.5 # pauses for 1 and a half secs

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene fast_food entrance
    with fade

    play LoNoise bgm_rest # plays background music

    pause 1.0

    m "Hmm is this the right place?"

    m "I'll ask the girl standing there."

    m "Uh hey is this the humble sandwich shop?"
 
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Reina neutral at center:
        yalign 1.3 zoom 0.65
    with dissolve   

    # These display lines of dialogue.

    b "Huh?"

    b "Oh, you must be the new recruit."

    m "Uh yeah."

    show Reina smile

    r "Welcome to the humble sandwich shop, I'm Reina"

    show Reina laugh 

    r "I look forward to working with you!"

    m "Same here"

    show Reina smile

    r "Since you're here already so early, I can be the one to show you around today."


    ### First Dialogue Branch ###
    menu: 

        r "Sooooo, do you think you have what it takes to makes sandwiches here?"


        "I think so.":

            jump yes

        "I've never made a sandwich in my entire life. Please Help.":

            jump no

label yes:

    show Reina laugh

    r "Awesome. I'm sure you'll do just fine here at the humble sandwich shop!"

    m "Damn right!"

    stop LoNoise
    play sound trans1
    jump inside
   


label no:

    show Reina wink

    r "Oh really? I've been wanting to teach a newbie."
        
    r "Ok that settles it. After I show around, I show you how we make our sandwiches here."

    r "Don't worry I know you'll do great!"

    m "Ok"

    "Damn I was hoping I could get someone else to teach me."

    stop LoNoise 
    play sound trans1
    jump inside

    

    #### Game continues after choice ###
    label inside:
        
        pause 4.0
        scene fast_food_interior_day
        with fade
        play LoNoise bgm_rest

        r "Here we have the inside of the beatiful humble sandwich shop!"
        
        show Reina smile at center:
            yalign 1.3 zoom 0.65
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

        stop LoNoise
        play sound trans1

        ############ Post-Tutorial #############

        pause 4.0

        scene fast_food_interior_day
        with fade

        play LoNoise bgm_rest

        pause 0.5

        show Reina smile at center:
            yalign 1.3 zoom 0.65
        with dissolve

        r "Wow, you built those sandwiches with conviction!"

        r "I just know you'll do great here."

        b "Never cease to show up super early, huh Reina?"
        
        # Allows charcter that was previously in the middle shift over to 
        # the right in order to make way for the other charcheter that entered the scene
        show Reina:
            linear 1.0 xalign 0.75 xzoom -1

        pause 1.0

        show Boss normal:
            zoom 0.85 xalign 0.25 yalign 0.35
        with dissolve

        pause 0.5

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

        stop LoNoise
        play sound trans1


        
        # End of first day after first level

        pause 4.0

        scene fast_food_entrance_day
        with fade

        play LoNoise bgm_rest

        show Reina smile at center:
            yalign 1.3 zoom 0.65
        with dissolve

        r "Good work today newbie, you didn't do half bad."

        show Reina laugh

        r "It'll only get better, I just know it!"

        show Reina smile

        r "Well see tomorrow newbie."


    # This ends the game.

    return
