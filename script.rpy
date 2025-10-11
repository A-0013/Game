# Combined Sandwich Game Script for Ren'Py

# Character Definitions
define e = Character("Eileen")

# Reina Ch images
image Reina_norm neutral = "images/people_reina_neutral_casual1.png"
image Reina_work neutral = "images/people_reina_neutral_work1.png"
image Reina_norm talk = "images/people_reina_neutral_open_casual1.png"
image Reina_work talk = "images/people_reina_neutral_open_work1.png"
image Reina_norm smile = "images/people_reina_happy_casual1.png"
image Reina_work smile = "images/people_reina_happy_work1.png"
image Reina_work angry = "images/people_reina_angry_work1.png"

# Boss Ch images
image Boss neutral = "images/people_boss_neutral1.png"
image Boss talk = "images/people_boss_neutral_open.png"
image Boss angry = "images/people_boss_angry.png"
image Boss happy = "images/people_boss_happy.png"

# Background images
image bg kitchen = "images/environment_interior.png"
image shop outside = "images/environment_exterior1.png"
image shop inside = "images/environment_interior.png"

# Audio definitions
define audio.bgm_rest = "audio/Time_for_Rest.ogg"
define audio.dialogue = "Characters/reina/audio/pack1/DialogueSFX/bleep_main.ogg"
define audio.trans1 = "Characters/reina/audio/pack1/Transitions/ogg/Transition_main.ogg"

# Game Variables
default placed_parts = []
default has_won = False
default pb_spawned = False
default jam_spawned = False
default score = 0
default show_finish_menu = False
default bread_spawns = []
default peanut_spawns = []
default jam_spawns = []
default lettuc_spawns = []
default tomato_spawns = []
default onion_spawns = []
default bacon_spawns = []
default cheese_spawns = []
default turkey_spawns = []
default mustard_spawns = []
default top_roll_spawns = []
default bottom_roll_spawns = []
default roll_click_count = True
default adder = 0
default required_sandwich = []
default placed_on_plate = set()
default time_left = 30
default game_over = False
default round_number = 1
default reached_level_5 = False
default bad_ending_triggered = False
default good_ending_triggered = False

# Callback function for text sounds
init python:
    import math
    
    # audio channels 
    renpy.music.register_channel("LoNoise","bgm") # BGM that loops 
    renpy.music.register_channel("trans1", "bgs", loop=False) # Transition (does not loop)
    renpy.music.register_channel("beep1", "sfx", loop=False) # Dialogue sfx (does not loop) 
    renpy.music.register_channel("victory", "sfx", loop=False) # Dialogue sfx (does not loop) 
    renpy.music.register_channel("defeat", "sfx", loop=False) # Dialogue sfx (does not loop)

    # This function makes continuous text sounds when characters speak
    def text_sounds(event, interact=True, **kwargs):
        if event == "show":
            what = renpy.store._last_say_what
            if what:
                sound_count = len(what)
            else:
                sound_count = 5
            for _ in range(sound_count):
                randosound = renpy.random.randint(1, 11)
                renpy.sound.queue(f"audio/pack1/DialogueSFX/bleep_main.ogg", channel="beep1", loop=False)
        elif event == "end" or event == "slow_done":
            renpy.sound.stop(channel="beep1")

# Character definitions using callback
define m = Character("MC", callback=text_sounds)
define r = Character("Reina", callback=text_sounds)
define b = Character("???", callback=text_sounds)
define d = Character("Don", callback=text_sounds)

# Game Logic
init python:
    import random
    
    # pool of ingredients
    INGREDIENTS = ["bacon", "bread", "jamm", "lettuc", "peanut", "tomato","onion", "mustard", "turkey", "cheese"]
    
    def spawn_bread():
        bread_count = len(store.bread_spawns)
        x_offset = (bread_count % 5) * 130
        y_offset = (bread_count // 5) * 130
        bread_id = "bread_" + str(bread_count)
        store.bread_spawns.append({
            'id': bread_id,
            'x': 1225,
            'y': 600
        })
        renpy.notify("🍞 Bread added to station!")
        renpy.restart_interaction()
        
    def spawn_peanut():
        peanut_count = len(store.peanut_spawns)
        peanut_id = "peanut_" + str(peanut_count)
        store.peanut_spawns.append({
            'id': peanut_id,
            'x': 1225,
            'y': 600
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
            'x': 1225,
            'y': 600
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
            'x': 1225,
            'y': 600
        })
        renpy.notify("🥬 Fresh lettuce added!")
        renpy.restart_interaction()
    
    def spawn_cheese():
        cheese_count = len(store.cheese_spawns)
        x_offset = (cheese_count % 5) * 130
        y_offset = (cheese_count // 5) * 130
        cheese_id = "cheese_" + str(cheese_count)
        store.cheese_spawns.append({
            'id': cheese_id,
            'x': 1225,
            'y': 600
        })
        renpy.notify("Fresh cheese added!")
        renpy.restart_interaction()
        
    def spawn_turkey():
        turkey_count = len(store.turkey_spawns)
        x_offset = (turkey_count % 5) * 130
        y_offset = (turkey_count // 5) * 130
        turkey_id = "turkey_" + str(turkey_count)
        store.turkey_spawns.append({
            'id': turkey_id,
            'x': 1225,
            'y': 600
        })
        renpy.notify("Fresh turkey added!")
        renpy.restart_interaction()
        
    def spawn_mustard():
        mustard_count = len(store.mustard_spawns)
        x_offset = (mustard_count % 5) * 130
        y_offset = (mustard_count // 5) * 130
        mustard_id = "mustard_" + str(mustard_count)
        store.mustard_spawns.append({
            'id': mustard_id,
            'x': 1225,
            'y': 600
        })
        renpy.notify("Fresh mustard added!")
        renpy.restart_interaction()
        
        
    def spawn_tomato():
        tomato_count = len(store.tomato_spawns)
        x_offset = (tomato_count % 5) * 130
        y_offset = (tomato_count // 5) * 130
        tomato_id = "tomato_" + str(tomato_count)
        store.tomato_spawns.append({
            'id': tomato_id,
            'x': 1225,
            'y': 600
        })
        renpy.notify("🍅 Tomato sliced!")
        renpy.restart_interaction()

    def spawn_onion():
        onion_count = len(store.onion_spawns)
        x_offset = (onion_count % 5) * 130
        y_offset = (onion_count // 5) * 130
        onion_id = "onion_" + str(onion_count)
        store.onion_spawns.append({
            'id': onion_id,
            'x': 1225,
            'y': 600
        })
        renpy.notify("Onion sliced!")
        renpy.restart_interaction()
        
    def spawn_bacon():
        bacon_count = len(store.bacon_spawns)
        x_offset = (bacon_count % 5) * 130
        y_offset = (bacon_count // 5) * 130
        bacon_id = "bacon_" + str(bacon_count)
        store.bacon_spawns.append({
            'id': bacon_id,
            'x': 1225,
            'y': 600
        })
        renpy.notify("🥓 Crispy bacon ready!")
        renpy.restart_interaction()
    
    def spawn_bread_roll():
        """Alternates between spawning top roll (odd clicks) and bottom roll (even clicks)"""
        store.roll_click_count = not(store.roll_click_count)  # Toggle between True/False
        
        if store.roll_click_count == True:  # Odd click - spawn top roll
            top_count = len(store.top_roll_spawns)
            x_offset = (top_count % 5) * 130
            y_offset = (top_count // 5) * 130
            roll_id = "top_roll_" + str(top_count)
            store.top_roll_spawns.append({
                'id': roll_id,
                'x': 1225,
                'y': 600
            })
            renpy.notify("🍞 Top roll added!")
        else:  # Even click - spawn bottom roll
            bottom_count = len(store.bottom_roll_spawns)
            x_offset = (bottom_count % 5) * 130
            y_offset = (bottom_count // 5) * 130
            roll_id = "bottom_roll_" + str(bottom_count)
            store.bottom_roll_spawns.append({
                'id': roll_id,
                'x': 1225,
                'y': 600
            })
            renpy.notify("🍞 Bottom roll added!")
        
        renpy.restart_interaction()
    
    def make_random_sandwich():
        # length grows each round, starting at 4
        length = 3 + store.round_number
        use_roll = random.choice([True, False])
        # Sandwich structure setup
        middle = random.choices([i for i in INGREDIENTS if i not in ["bread", "top_roll", "bottom_roll"]], k=length - 2)
        if use_roll:
            # Use rolls as top and bottom
            sandwich = ["bottom_roll"] + middle + ["top_roll"]
        else:
            # Use bread as top and bottom
            sandwich = ["bread"] + middle + ["bread"]
        
        return sandwich

    def clear_plate():
        store.placed_parts = []
        store.placed_on_plate = set()
        renpy.notify("🧹 Plate cleared! Ready for new order!")
        renpy.restart_interaction()
    
    def clear_cutting_board():
        store.bread_spawns = []
        store.peanut_spawns = []
        store.jam_spawns = []
        store.lettuc_spawns = []
        store.tomato_spawns = []
        store.bacon_spawns = []
        store.onion_spawns = []
        store.cheese_spawns = []
        store.turkey_spawns = []
        store.mustard_spawns = []
        store.top_roll_spawns = []
        store.bottom_roll_spawns = []
        store.roll_click_count = True
        renpy.notify("🗑️ Cutting board cleared!")
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
            elif drag.drag_name.startswith("onion_"):
                ingredient_name = "onion"
            elif drag.drag_name.startswith("cheese_"):
                ingredient_name = "cheese"
            elif drag.drag_name.startswith("mustard_"):
                ingredient_name = "mustard"
            elif drag.drag_name.startswith("turkey_"):
                ingredient_name = "turkey"
            elif drag.drag_name.startswith("bacon_"):
                ingredient_name = "bacon"
            elif drag.drag_name.startswith("top_roll_"):
                ingredient_name = "top_roll"
            elif drag.drag_name.startswith("bottom_roll_"):
                ingredient_name = "bottom_roll"
                
            # Always add each ingredient separately (allows duplicates)
            store.placed_parts.append(ingredient_name)
            store.placed_on_plate.add(ingredient_name)
            
            # Remove the dragged ingredient from its spawn list
            remove_ingredient_from_spawns(drag.drag_name)
            
            # Enhanced feedback with emojis
            renpy.notify("✅ Added " + ingredient_name.title() + " (" + str(len(store.placed_parts)) + "/" + str(len(store.required_sandwich)) + ")")
            
            # refresh screen so HUD updates
            renpy.restart_interaction()
            
            # check win condition - compare lists exactly
            if len(store.placed_parts) == len(store.required_sandwich):
                if store.placed_parts == store.required_sandwich:
                    store.has_won = True
                    points = round_number * round(30.0/max(time_left, 1))
                    store.score += points
                    
                    # Check for good ending (completed level 5 or higher)
                    if store.round_number >= 5:
                        store.good_ending_triggered = True
                        renpy.notify("🎉 Perfect! You've mastered the art of sandwich making! Good ending unlocked!")
                    else:
                        renpy.notify("🎉 Perfect! Order complete! Score: " + str(store.score))
                    renpy.restart_interaction()
                else:
                    renpy.notify("❌ Order doesn't match! Check the required ingredients!")
    
    def remove_ingredient_from_spawns(ingredient_id):
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
        elif ingredient_id.startswith("onion_"):
            store.onion_spawns = [item for item in store.onion_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("cheese_"):
            store.cheese_spawns = [item for item in store.cheese_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("mustard_"):
            store.mustard_spawns = [item for item in store.mustard_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("turkey_"):
            store.turkey_spawns = [item for item in store.turkey_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("bacon_"):
            store.bacon_spawns = [item for item in store.bacon_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("top_roll_"):
            store.top_roll_spawns = [item for item in store.top_roll_spawns if item['id'] != ingredient_id]
        elif ingredient_id.startswith("bottom_roll_"):
            store.bottom_roll_spawns = [item for item in store.bottom_roll_spawns if item['id'] != ingredient_id]
    
    def start_new_order():
        store.placed_parts = []
        store.placed_on_plate = set()
        store.has_won = False
        store.round_number += 1
        
        # Track when player reaches level 5
        if store.round_number == 5:
            store.reached_level_5 = True
            renpy.notify("🌟 Level 5 reached! This is where things get serious...")
        
        store.required_sandwich = make_random_sandwich()
        store.time_left = 30
        store.game_over = False
        store.bread_spawns = []
        store.peanut_spawns = []
        store.jam_spawns = []
        store.lettuc_spawns = []
        store.tomato_spawns = []
        store.onion_spawns = []
        store.bacon_spawns = []
        store.cheese_spawns = []
        store.turkey_spawns = []
        store.mustard_spawns = []
        store.top_roll_spawns = []
        store.bottom_roll_spawns = []
        store.roll_click_count = True
        renpy.notify("📋 Round " + str(store.round_number) + " - New order incoming! Score: " + str(store.score))
        renpy.restart_interaction()
    
    def continue_current_level():
        store.placed_parts = []
        store.placed_on_plate = set()
        store.has_won = False
        store.required_sandwich = make_random_sandwich()
        store.time_left = 30
        store.game_over = False
        store.bread_spawns = []
        store.peanut_spawns = []
        store.jam_spawns = []
        store.lettuc_spawns = []
        store.tomato_spawns = []
        store.onion_spawns = []
        store.bacon_spawns = []
        store.cheese_spawns = []
        store.turkey_spawns = []
        store.mustard_spawns = []
        store.top_roll_spawns = []
        store.bottom_roll_spawns = []
        store.roll_click_count = True
        renpy.notify("🔄 Level " + str(store.round_number) + " restarted! Try again!")
        renpy.restart_interaction()

    def check_done():
        try:
            if not required_sandwich:
                renpy.notify("No order selected.")
                return
            placed = list(placed_parts)
            wrong = [p for p in placed if p not in required_sandwich]
            if wrong:
                renpy.notify("Wrong ingredient present: " + ", ".join(wrong))
                return
            missing = [r for r in required_sandwich if r not in placed]
            if missing:
                renpy.notify("Missing: " + ", ".join(missing))
                return
            store.has_won = True
            store.score += 1
            renpy.notify("You won! Score: " + str(store.score))
            renpy.restart_interaction()
        except Exception as e:
            renpy.notify("Error checking order.")
            renpy.log(str(e))

# The game starts here
label start:
    pause 1.5

    scene shop outside
    with fade

    play LoNoise bgm_rest

    pause 1.0

    m "Hmm is this the right place?"

    m "I'll ask the girl standing there."

    m "Uh hey is this the humble sandwich shop?"

    show Reina_norm neutral at center:
        yalign 1.3 zoom 0.65
    with dissolve

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
    
    window hide
    $ renpy.pause(4.0, hard=True)

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
    
    window hide
    $ renpy.pause(4.0, hard=True)

    jump inside

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

    window hide
    $ renpy.pause(4.0, hard=True)

    # Reset game variables for first gameplay
    $ placed_parts = []
    $ has_won = False
    $ pb_spawned = False
    $ jam_spawned = False
    $ show_finish_menu = False
    $ bread_spawns = []
    $ peanut_spawns = []
    $ jam_spawns = []
    $ lettuc_spawns = []
    $ tomato_spawns = []
    $ bacon_spawns = []
    $ required_sandwich = make_random_sandwich()
    $ placed_on_plate = set()
    $ round_number = 1
    $ time_left = 30
    $ game_over = False

    scene bg kitchen
    "beach sorcestor time"
    
    call screen sandwich_game

    # Post-Tutorial
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

    window hide
    $ renpy.pause(4.0, hard=True)
    
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

    return

############ END OF GAME #############

### Good Ending Scene ###
label good_ending:
    scene shop outside
    with fade

    play LoNoise bgm_rest

    show Reina_norm talk at center:
        yalign 1.3 zoom 0.65
    with dissolve

    r "Good work today newbie, you did great"

    show Reina_norm smile

    r "It'll only get better, I just know it!"

    d "She's right you know."

    show Reina_norm smile:
        linear 1.0 xalign 0.75 xzoom -1

    pause 1.0

    show Boss happy:
        zoom 0.85 xalign 0.25 yalign 0.35
    with dissolve

    pause 0.5

    d "I was observing how you made those sandwiches and you didn't do half bad."

    d "Y'know, there is some real untapped potential there."

    d "Continue to work hard and you may someday surpass Reina."

    r "Hehe, like that'll ever happen."

    d "Anyways, keep up the good work kid and welcome to the team."

    r "Well, see tomorrow newbie!"

    m "Thanks, see you tomorrow!"

    stop LoNoise
    #play sound victory

    # Hide window and block input for 4 seconds
    window hide
    $ renpy.pause(4.0, hard=True)

    # This ends the game.
    return

### Bad Ending Scene ###
label bad_ending:
    scene shop outside
    with fade

    play LoNoise sadPiano

    show Reina_norm sad at center:
        yalign 1.3 zoom 0.65 
    with dissolve

    pause 0.5

    r "You really messed up today newbie..."

    r "I don't know how its possible to mess up such simple orders..."

    r "The Boss is really mad at you now."

    show Reina_norm sad:
        linear 1.0 xalign 0.75 xzoom -1

    pause 1.0

    show Boss sad:
        zoom 0.85 xalign 0.25 yalign 0.35
    with dissolve

    pause 0.5

    d "Sigh..."

    d "Never in my life have I felt so disrespected."

    d "You're fired kid."

    d "Good luck on your futrue endeavors."

    show Boss neutral

    d "But also..."

    show Boss angry

    d "Get out of my sight before I clobber you."

    r "Well, see you never newbie..."

    m "Damn..."

    stop LoNoise
    play sound defeat

    # Hide window and block input for 4 seconds
    window hide
    $ renpy.pause(4.0, hard=True)

    # This ends the game.
    return