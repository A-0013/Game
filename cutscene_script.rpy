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
                renpy.sound.queue(f"audio/pack1/DialogueSFX/bleep_main.ogg", channel="beep1", loop=False)
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

    scene shop outside
    with fade

    play LoNoise bgm_rest # plays background music

    pause 1.0

    m "Hmm is this the right place?"

    m "I'll ask the girl standing there."

    m "Uh hey is this the humble sandwich shop?"
 
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Reina_norm neutral at center:
        yalign 1.3 zoom 0.65
    with dissolve   

    # These display lines of dialogue.

    b "Huh?"

    show Reina_norm talk

    b "Oh, you must be the new recruit."
    
    show Reina_norm neutral

    m "Uh, yeah."

    show Reina_norm smile

    r "Welcome to the humble sandwich shop, I'm Reina."

    r "I look forward to working with you!"

    m "Same here."

    show Reina_norm talk

    r "Since you showed up earlier than expected, I can be the one to show you around today."


    ### First Dialogue Branch ###
    menu: 

        r "Sooooo, do you think you have what it takes to makes sandwiches here?"


        "I think so.":

            jump yes

        "I've never made a sandwich in my entire life. Please help.":

            jump no

label yes:

    show Reina_norm smile

    r "Awesome. I'm sure you'll do just fine here at the humble sandwich shop!"

    m "Damn right!"

    stop LoNoise
    play sound trans1
    
    # Hide window and block input for 4 seconds
    window hide
    $ renpy.pause (4.0, hard=True)

    jump inside
   


label no:

    show Reina_norm smile

    r "Oh really? I've been wanting to teach a newbie."
        
    r "Ok that settles it. After I show around, I'll also show you how we make our sandwiches here."

    r "Don't worry I know you'll do great!"

    m "Ok"

    "Damn I was hoping I could get someone else to teach me."

    stop LoNoise 
    play sound trans1
    jump inside
    
    # Hide window and block input for 4 seconds
    window hide
    $ renpy.pause (4.0, hard=True)

    #### Game continues after choice ###
    label inside: 
        
        scene shop inside
        with fade
        play LoNoise bgm_rest

        r "Here we have the inside of the beatiful humble sandwich shop!"
        
        show Reina_work smile at center:
            yalign 1.3 zoom 0.65
        with dissolve

        r "Pretty cool huh?"

        show Reina_work neutral

        m "It's pretty neat I guess."

        show Reina_work talk

        r "So you're new to the art of sandwich making huh?"
        
        show Reina_work neutral

        m "Apparently..."

        show Reina_work smile

        r "Well it's a good thing you ran into me first. I'll have you know I'm best the sandwich builder in the shop."

        r "No one can do it better than me. I'll be happy to show you the ropes."

        show Reina_work talk

        r "Ok lets get to sandwich making!"

        r "We'll start by making a basic PB&J and BLT!"

        "You could speak at a normal volume y'know..."

        show Reina_work smile

        r "Pay attention now. Game mechanics are coming in hot!"

        r "Use you mouse to drag and drop the items in the correct order."

        r "It's as simple as that!"

        stop LoNoise
        play sound trans1

        # Hide window and block input for 4 seconds
        window hide
        $ renpy.pause (4.0, hard=True)

        ############ Post-Tutorial #############


        scene shop inside
        with fade

        play LoNoise bgm_rest

        pause 0.5

        show Reina_work smile at center:
            yalign 1.3 zoom 0.65
        with dissolve

        r "Wow, you built those sandwiches with conviction!"

        r "I just know you'll do great here."

        show Reina_work neutral

        b "Never cease to show up super early, huh Reina?"
        
        # Allows charcter that was previously in the middle shift over to 
        # the right in order to make way for the other charcheter that entered the scene
        show Reina_work neutral:
            linear 1.0 xalign 0.75 xzoom -1

        pause 1.0

        show Boss neutral:
            zoom 0.85 xalign 0.25 yalign 0.35
        with dissolve

        pause 0.5

        show Reina_work smile

        r "Hehe you know me, I just can't get enough of this place!"

        show Reina_work neutral

        r "By the way, the new hire got here early too. I was showing them how it's done."

        
        # Second Dialogue Branch

        menu: 

            "Wait, is this guy the boss?":

                jump respect

            "Hey Reina, who's this old guy?":

                jump disrespect


    label respect:
        
        show Reina_work smile

        r "Yup, this is Don. He's the guy who built this place from the ground up."

        show Boss talk 

        d "Good to meet you kid."

        d "I've been in this business for a while and while some may say I'm getting old..."

        show Boss happy

        d "I prefer the term, experienced."

        jump continue

    label disrespect:

        show Reina_work angry

        r "Newbie, that was definitely a question you just asked."

        show Reina_work talk

        r "This is Don. He's the boss here and he built this place from the ground up."

        show Boss talk

        d "Heh, old is one thing kid, but I prefer the term..."

        show Boss angry

        d "Experienced."

        jump continue

    

    label continue:
        
        show Reina_work neutral

        show Boss talk

        d "So, seems like Reina taught you all the basics."

        d "Here's a word of advice kid."
        
        show Boss angry

        d "Never underestimate customers and their orders."

        show Boss neutral

        "Heh, of course I know that. Sooner or later, I'll be the one telling new hires that."

        d "Ok, we should be opening soon."

        show Reina_work smile

        r "Yes, time for your first day to truly begin newbie!"

        r "Good luck!"

        stop LoNoise
        play sound trans1

        # Hide window and block input for 4 seconds
        window hide
        $ renpy.pause (4.0, hard=True)
        
        # End of first day after first level


        scene shop outside
        with fade

        play LoNoise bgm_rest

        show show Reina_norm talk at center:
            yalign 1.3 zoom 0.65
        with dissolve

        r "Good work today newbie, you didn't do half bad."

        show Reina_norm smile

        r "It'll only get better, I just know it!"

        r "Well, see tomorrow newbie."


    # This ends the game.

    return
