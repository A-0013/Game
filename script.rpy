#came with file not touching
define e = Character("Eileen")

# Reina Ch images
image Reina_norm neutral = "images/Characters/reina/people_reina_neutral_casual.png"
image Reina_work neutral = "images/Characters/reina/people_reina_neutral_work.png"
image Reina_norm talk = "images/Characters/reina/people_reina_neutral_open_casual.png"
image Reina_work talk = "images/Characters/reina/people_reina_neutral_open_work.png"
image Reina_norm smile = "images/Characters/reina/people_reina_happy_casual.png"
image Reina_work smile = "images/Characters/reina/people_reina_happy_work.png"
image Reina_work angry = "images/Characters/reina/people_reina_angry_work.png"

# Boss Ch imgaes
image Boss neutral = "images/Characters/boss/people_boss_neutral1.png"
image Boss talk = "images/Characters/boss/people_boss_neutral_open.png"
image Boss angry = "images/Characters/boss/people_boss_angry.png"
image Boss happy = "images/Characters/boss/people_boss_happy.png"

# Background images
image bg kitchen = "bg_imagesMain/fast_food_interior_day.png"
image shop outside = "bg_imagesMain/fast_food_entrance_day.png"
image shop inside = "bg_imagesMain/fast_food_interior_day.png"

# Audio definitions
define audio.bgm_rest = "Characters/reina/audio/pack1/bgm/ogg/Time_for_Rest.ogg"
define audio.dialogue = "Characters/reina/audio/pack1/DialogueSFX/bleep_main.ogg"
define audio.trans1 = "Characters/reina/audio/pack1/Transitions/ogg/Transition_main.ogg"
#the variables
default placed_parts = []
#if I didnt write it twice it would hate me
default has_won = False
default pb_spawned = False
default jam_spawned = False
default score = 0  # Add score tracking
default show_finish_menu = False  # New variable for finish menu
#yes I did actually do this manually
default bread_spawns = []  # List to track spawned bread
default peanut_spawns = []  # List to track spawned peanut butter
default jam_spawns = []  # List to track spawned jelly
default lettuc_spawns = []  # List to track spawned lettuce
default tomato_spawns = []  # List to track spawned tomato
default bacon_spawns = []  # List to track spawned bacon
default required_sandwiches = []  # Now a list of 3 orders
default placed_on_plate = set()
default time_left = 30  # countdown timer
default game_over = False
default round_number = 1


#this is manually done change it later
#yeah I didn't lmao


# The game starts here.
label start:
    #resets everything except score
    $ placed_parts = []
    $ has_won = False
    $ pb_spawned = False
    $ jam_spawned = False
    $ show_finish_menu = False
    #more manual work
    $ bread_spawns = []  # Reset bread spawns
    $ peanut_spawns = []  # Reset peanut butter spawns
    $ jam_spawns = []  # Reset jelly spawns
    $ lettuc_spawns = []  # Reset lettuce spawns
    $ tomato_spawns = []  # Reset tomato spawns
    $ bacon_spawns = []  # Reset bacon spawns
    $ required_sandwiches = [make_random_sandwich() for _ in range(3)]  # Generate 3 orders
    $ placed_on_plate = set()  # Reset placed items
    $ round_number = 1
    # Kitchen time
    scene bg kitchen
    # Sand witch pun (it's so bad)
    "beach sorcestor time"
    # Tell player what to make
    call screen sandwich_game

init python:
    import random
    # pool of ingredients
    INGREDIENTS = ["bacon", "bread", "jamm", "lettuc", "peanut", "tomato"]

    def spawn_bread():
        bread_count = len(store.bread_spawns)
        #spread them loafs
        x_offset = (bread_count % 5) * 130  # 5 bread per row
        y_offset = (bread_count // 5) * 130  # New row every 5 bread (spamming bread in one place makes lag)
        bread_id = "bread_" + str(bread_count)
        store.bread_spawns.append({
            'id': bread_id,
            'x': 150 + x_offset,
            'y': 300 + y_offset
        })
        # Enhanced notification with emoji
        renpy.notify("🍞 Bread added to station!")
        renpy.restart_interaction()

    #more of the same
    def spawn_peanut():
        peanut_count = len(store.peanut_spawns)
        x_offset = (peanut_count % 5) * 130
        y_offset = (peanut_count // 5) * 130
        peanut_id = "peanut_" + str(peanut_count)
        store.peanut_spawns.append({
            'id': peanut_id,
            'x': 350 + x_offset,
            'y': 300 + y_offset
        })
        renpy.notify("🥜 Peanut butter ready!")
        renpy.restart_interaction()

    def spawn_jam():
        jam_count = len(store.jam_spawns)
        x_offset = (jam_count % 5) * 130
        y_offset = (jam_count // 5) * 130
        jam_id = "jamm_" + str(jam_count)
        store.jam_spawns.append({
            'id': jam_id,
            'x': 550 + x_offset,
            'y': 300 + y_offset
        })
        renpy.notify("🍇 Jelly prepared!")
        renpy.restart_interaction()

    def spawn_lettuce():
        lettuc_count = len(store.lettuc_spawns)
        x_offset = (lettuc_count % 5) * 130
        y_offset = (lettuc_count // 5) * 130
        lettuc_id = "lettuc_" + str(lettuc_count)
        store.lettuc_spawns.append({
            'id': lettuc_id,
            'x': 750 + x_offset,
            'y': 300 + y_offset
        })
        renpy.notify("🥬 Fresh lettuce added!")
        renpy.restart_interaction()

    def spawn_tomato():
        tomato_count = len(store.tomato_spawns)
        x_offset = (tomato_count % 5) * 130
        y_offset = (tomato_count // 5) * 130
        tomato_id = "tomato_" + str(tomato_count)
        store.tomato_spawns.append({
            'id': tomato_id,
            'x': 850 + x_offset,
            'y': 300 + y_offset
        })
        renpy.notify("🍅 Tomato sliced!")
        renpy.restart_interaction()

    def spawn_bacon():
        bacon_count = len(store.bacon_spawns)
        x_offset = (bacon_count % 5) * 130
        y_offset = (bacon_count // 5) * 130
        bacon_id = "bacon_" + str(bacon_count)
        store.bacon_spawns.append({
            'id': bacon_id,
            'x': 650 + x_offset,
            'y': 300 + y_offset
        })
        renpy.notify("🥓 Crispy bacon ready!")
        renpy.restart_interaction()

    def make_random_sandwich():
        # length grows each round, starting at 4
        length = 3 + store.round_number  # 1st round = 4, then 5, then 6, etc.
        # sandwich must always have at least 2 bread (first + last)
        middle = random.choices([i for i in INGREDIENTS if i != "bread"], k=length - 2)
        sandwich = ["bread"] + middle + ["bread"]
        return sandwich


    def clear_plate():
        # Just reset placed items
        store.placed_parts = []
        store.placed_on_plate = set()
        renpy.notify("🧹 Plate cleared! Ready for new order!")
        renpy.restart_interaction()


    def place_ingredient(drop_target, drags):
        drag = drags[0]
        if drop_target.drag_name == "plate":
            # Handle different ingredient IDs - convert back to base names
            ingredient_name = drag.drag_name
            if drag.drag_name.startswith("bread_"):
                ingredient_name = "bread"
            elif drag.drag_name.startswith("peanut_"):
                ingredient_name = "peanut"
            elif drag.drag_name.startswith("jamm_"):
                ingredient_name = "jamm"
            elif drag.drag_name.startswith("lettuc_"):
                ingredient_name = "lettuc"
            elif drag.drag_name.startswith("tomato_"):
                ingredient_name = "tomato"
            elif drag.drag_name.startswith("bacon_"):
                ingredient_name = "bacon"

            # Always add each ingredient separately (allows duplicates)
            store.placed_parts.append(ingredient_name)
            store.placed_on_plate.add(ingredient_name)

            # Remove the dragged ingredient from its spawn list so it doesn't reappear
            remove_ingredient_from_spawns(drag.drag_name)

            # Enhanced feedback with emojis
            renpy.notify("✅ Added " + ingredient_name.title() + " (" + str(len(store.placed_parts)) + "/" + str(len(store.required_sandwich)) + ")")

            # refresh screen so HUD updates
            renpy.restart_interaction()

            # check win condition - compare lists exactly
            if len(store.placed_parts) == len(store.required_sandwich):
                if store.placed_parts == store.required_sandwich:
                    store.has_won = True
                    store.score += (round_number * (30/(time_left)))  # Increment score
                    renpy.notify("🎉 Perfect! Order complete! Score: " + str(store.score))
                    renpy.restart_interaction()
                else:
                    # Enhanced error feedback
                    renpy.notify("❌ Order doesn't match! Check the required ingredients!")

    def remove_ingredient_from_spawns(ingredient_id):
        # Remove ingredient from appropriate spawn list
        if ingredient_id.startswith("bread_"):
            store.bread_spawns = [item for item in store.bread_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("peanut_"):
            store.peanut_spawns = [item for item in store.peanut_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("jamm_"):
            store.jam_spawns = [item for item in store.jam_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("lettuc_"):
            store.lettuc_spawns = [item for item in store.lettuc_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("tomato_"):
            store.tomato_spawns = [item for item in store.tomato_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("bacon_"):
            store.bacon_spawns = [item for item in store.bacon_spawns if item['id'] != ingredient_id]



    def start_new_order():
        # Clear the plate and generate new order
        store.placed_parts = []
        store.placed_on_plate = set()
        store.has_won = False
        store.round_number += 1  # INCREASE ROUND
        store.required_sandwich = make_random_sandwich()
        store.time_left = 30
        store.game_over = False
        # Clear all spawned ingredients
        store.bread_spawns = []
        store.peanut_spawns = []
        store.jam_spawns = []
        store.lettuc_spawns = []
        store.tomato_spawns = []
        store.bacon_spawns = []
        renpy.notify("📋 Round " + str(store.round_number) + " - New order incoming! Score: " + str(store.score))
        renpy.restart_interaction()


    def check_done():
        try:
            if not required_sandwich:
                renpy.notify("No order selected.")
                return
            # makes a list of ingredients on plate
            placed = list(placed_parts)
            #this is so overly complicated but it just makes sure the jelly sandwhich has jelly
            wrong = [p for p in placed if p not in required_sandwich]
            if wrong:
                renpy.notify("Wrong ingredient present: " + ", ".join(wrong))
                return
            missing = [r for r in required_sandwich if r not in placed]
            if missing:
                renpy.notify("Missing: " + ", ".join(missing))
                return
            # tells u u won
            store.has_won = True
            store.score += 1  # Increment score here too as backup
            renpy.notify("You won! Score: " + str(store.score))
            renpy.restart_interaction()
        except Exception as e:
            renpy.notify("Error checking order.")
            renpy.log(str(e))
            #this took so long ahhhhhhhhhhh


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

        show Reina_norm talk at center:
            yalign 1.3 zoom 0.65
        with dissolve

        r "Good work today newbie, you didn't do half bad."

        show Reina_norm smile

        r "It'll only get better, I just know it!"

        r "Well, see tomorrow newbie."


    # This ends the game.

    return
