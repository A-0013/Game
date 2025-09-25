
#came with file not touching
define e = Character("Eileen")

#the variables
default placed_parts = []
#if I didnt write it twice it would hate me
default has_won = False
default pb_spawned = False
default jam_spawned = False
default required_sandwich = []
default placed_on_plate = set()

#this is manually done change it later

# The game starts here.
label start:
    #resets everything
    $ placed_parts = []
    $ has_won = False
    $ pb_spawned = False
    $ jam_spawned = False
    #$ sandwich_type = renpy.random.choice(["bacon", "bread", "jamm","lettuc","peanut","tomato"])
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
            if drag.drag_name not in placed_parts:
                placed_parts.append(drag.drag_name)
                store.placed_on_plate.add(drag.drag_name)

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

            #this is so overly complicated but it just makes sure the jelly sandwhich doesnt have jelly
            wrong = [p for p in placed if p not in required_sandwich]
            if wrong:
                renpy.notify("Wrong ingredient present: " + ", ".join(wrong))
                return

            # makes sure the jelly sanwhcih has jelly
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