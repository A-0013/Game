# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")

default pb_spawned = False
default jam_spawned = False
default has_won = False
default placed_parts = []


# The game starts here.
label start:
    #make a 'set' of sandwhich pieces (when all the pieces of the set are together its a win)
    $ placed_parts = set()
    #set has won to false so that way repeat play thrus possible
    $ has_won = False
    #kitchen time
    scene bg kitchen
    #sand witch pun (its so bad)
    "beach sorcestor time"
    #call the game screen
    call screen sandwich_game

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