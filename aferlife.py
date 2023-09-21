## Introduction
def purgatory():
    directions = ["left", "right"]
    print("Hey, sorry to be the bearer of bad news, but you've just died.")
    print("Our moral judgement systems are currently down, so you’ll have to decide whether you end up in heaven or hell.")
    print("Also I forgot which door is which, so, um...")
    print("Please pick a door.")
    response = ""
    while response not in directions:
        response = input("Which door do you pick? Options: left/right ")
        if response == "left":
            welcome_to_hell()
        elif response == "right":
            welcome_to_heaven()
        else: 
            print("Please enter left or right.")

## If user picks left in purgatory, it launches the hell route
def welcome_to_hell():
    print("You open the door on the left. Behind it is a red figure with horns on his head and a pointy tail snaking behind his back.")
    print("\"Welcome to hell!\" the devil greets you. \"Let me give you a tour of our facilities.\"")
    hell_lobby()

## Hell's main room
def hell_lobby():
    directions = ["left", "right", "forwards", "backwards"]
    print("\"Where would you like to go?\"")
    response = ""
    while response not in directions:
        response = input("Options: left/right/forwards/backwards ")
        if response == "left":
            print("\"Here they are, our famous fiery pits!\"")
            print("You wipe the sweat off your forehead as you wander the perimiter, staying as far away from the edge as possible.")
            hell_lobby()
        elif response == "right":
            print("\"Here's where we keep our fuzzy friends!\" the devil says as you pass a maggot petting zoo.")
            print("You feel a bit sick.")
            hell_lobby()
        elif response == "forwards":
            print("'Follow me!'")
            follow_devil()
        elif response == "backwards":
            print("You desperately try to open the door behind you only to find it locked.") 
            print("The devil grabs you. \"Leaving so soon?'\" they ask before throwing you into the fiery pits.")
            print("You spend an eternity trying to get used to the heat.")
            game_over()
        else: 
            print("Please enter left, right, forwards or backwards.")

## Hell's cliffside
def follow_devil():
    directions = ["forwards", "backwards"]
    print("You shuffle behind the devil until you come to the edge of a cliff.")
    print("\"Well, here's your room,\" he says. \"Just jump on in when you're ready, make yourself at home.\"")
    response = ""
    while response not in directions:
        response = input("Where do you go? Options: forwards/backwards ")
        if response == "backwards":
            print("You still want to explore some more.")
            hell_lobby()
        elif response == "forwards":
            print("Here goes nothing.")
            print("You jump.")
            print("You fall down, down, down into the darkness.")
            print("It keeps going.")
            print("You're still going down.")
            print("It's starting to get boring, really.")
            print("Suddenly, a blinding light fills the abyss.")
            hell_to_heaven()
        else: 
            print("Please enter forwards or backwards.")

## Hell to heaven route introduction
def hell_to_heaven():
    print("You hit the ground with a thud. Surprisingly, it didn't hurt.")
    print("You look up. Standing above you is a figure dressed in white with a halo over his head and wings behind his back.")
    print("\"Welcome to heaven!\" the angel greets you. \"Let me give you a tour of our facilities.\"")
    heaven_lobby()

## If user picks right in purgatory, it launches the heaven route
def welcome_to_heaven():
    print("You open the door on the left. Behind it is a figure dressed in white with a halo over his head and wings behind his back.")
    print("\"Welcome to heaven!\" the angel greets you. \"Let me give you a tour of our facilities.\"")
    heaven_lobby()

## Heaven's main room
def heaven_lobby():
    directions = ["left", "right", "forwards", "backwards"]
    print("\"Where would you like to go?\"")
    response = ""
    while response not in directions:
        response = input("Options: left/right/forwards/backwards ")
        if response == "left":
            print("\"Here are our candy gardens, recently rennovated. Feel free to take a bite of anything!\"")
            print("You see cotton candy trees and grand chocolate fountains.")
            heaven_lobby()
        elif response == "right":
            print("\"Here's where we keep our magical friends!\" the angel says as you pass the unicorn stables.")
            print("In the distance, you see unicorns flying over rainbows.")
            heaven_lobby()
        elif response == "forwards":
            print("'Follow me!'")
            follow_angel()
        elif response == "backwards":
            print("You turn around and see the door behind you.") 
            print("The angel puts a hand on your shoulder. \"Don't worry, it's locked,\" he smiles. \"Now, time to go and enjoy your afterlife.\"")
            print("You spend an eternity in relaxing bliss. Your back never hurts and every day is a good hair day.")
            game_over()
        else: 
            print("Please enter left, right, forwards or backwards.")


## Heaven's cloud beds
def follow_angel():
    directions = ["forwards", "backwards"]
    print("You shuffle behind the angel until you come to a field of clouds, all hovering low above the ground.")
    print("\"Well, here's your cloud bed,\" he says as he points to one. \"Just jump on when you're ready, make yourself comfortable.\"")
    response = ""
    while response not in directions:
        response = input("Where do you go? Options: forwards/backwards ")
        if response == "backwards":
            print("You still want to explore some more.")
            heaven_lobby()
        elif response == "forwards":
            print("You jump onto the cloud and lie down.")
            print("You sink into fluffy bliss as you feel yourself gently floating away.")
            print("Suddenly, things aren't so gentle.")
            print("You're not floating anymore, you're falling.")
            print("You're going down fast.")
            print("Suddenly, you're surrounded by darkness.")
            heaven_to_hell()
        else: 
            print("Please enter forwards or backwards.")

## Heaven to hell route introduction
def heaven_to_hell():
    print("You hit the ground with a thud. Oof, that hurt.")
    print("You look up. Standing above you is a red figure with horns on his head and a pointy tail snaking behind his back.")
    print("\"Welcome to hell!\" the devil greets you. \"Let me give you a tour of our facilities.\"")
    hell_lobby()

## Game over function gives player the option to start again
def game_over():
    directions = ["yes", "no"]
    print("Game over.")
    response = ""
    while response not in directions:
        response = input("Would you like another shot at the afterlife? Options: yes/no ")
        if response == "yes":
            purgatory()
        elif response == "no":
            print("Have a great eternity!")
        else:
            print("Please enter yes or no.")

## Calling the function to start the game
purgatory()