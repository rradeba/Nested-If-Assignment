# Task 1 -3 
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark?  ")
    if cave_action == "light a torch":
        print("Over there, it's the treasure!")
    elif cave_action == "proceed in the dark"   : 
        print("It is too dark to see in here!")
    else:
        pass
else:
    pass

