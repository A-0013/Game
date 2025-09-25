#came with file not touching
define e = Character("Eileen")
#the variables
default placed_parts = []
#if I didnt write it twice it would hate me
default has_won = False
default pb_spawned = False
default jam_spawned = False
#yes I did actually do this manually
default bread_spawns = []  # List to track spawned bread 
default peanut_spawns = []  # List to track spawned peanut butter 
default jam_spawns = []  # List to track spawned jelly 
default lettuc_spawns = []  # List to track spawned lettuce 
default tomato_spawns = []  # List to track spawned tomato 
default bacon_spawns = []  # List to track spawned bacon 
default required_sandwich = []
default placed_on_plate = set()
#this is manually done change it later
#yeah I didn't lmao


# The game starts here.
label start:
    #resets everything
    $ placed_parts = []
    $ has_won = False
    $ pb_spawned = False
    $ jam_spawned = False
    #more manual work
    $ bread_spawns = []  # Reset bread spawns
    $ peanut_spawns = []  # Reset peanut butter spawns
    $ jam_spawns = []  # Reset jelly spawns
    $ lettuc_spawns = []  # Reset lettuce spawns
    $ tomato_spawns = []  # Reset tomato spawns
    $ bacon_spawns = []  # Reset bacon spawns
    $ required_sandwich = make_random_sandwich()
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
        # Debug notification (very necessary)
        renpy.notify("Spawned bread! Total: " + str(len(store.bread_spawns)))
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
        renpy.notify("Spawned peanut butter!")
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
        renpy.notify("Spawned jelly!")
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
        renpy.notify("Spawned lettuce!")
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
        renpy.notify("Spawned tomato!")
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
        renpy.notify("Spawned bacon!")
        renpy.restart_interaction()
    
    def make_random_sandwich():
        # sandwich must be 3–6 ingredients
        length = random.randint(3, 6)
        # at least 2 slots will be bread (first + last)
        # fill the middle with random ingredients (no restriction on repeats, unless you want unique)
        middle = random.choices([i for i in INGREDIENTS if i != "bread"], k=length - 2)
        sandwich = ["bread"] + middle + ["bread"]
        return sandwich
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
            placed_parts.append(ingredient_name)
            store.placed_on_plate.add(ingredient_name)
            
            # refresh screen so HUD updates
            renpy.restart_interaction()
            # check win condition
            if placed_parts == required_sandwich:
                store.has_won = True
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
            renpy.notify("You won!")
            renpy.restart_interaction()
        except Exception as e:
            renpy.notify("Error checking order.")
            renpy.log(str(e))
            #this took so long ahhhhhhhhhhh