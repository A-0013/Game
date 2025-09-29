#came with file not touching
define e = Character("Eileen")
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
