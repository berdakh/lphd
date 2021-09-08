from sys import exit 
#% This script shows the interaction of 5 (five) different functions...
# in one python script to implement a game :)))) 
def gold_room():
    print("This room is full of gold. How much do you take in")
    how_much = int(input("> "))
#    if "0" in choice or "1" in choice:
#        how_much = int(choice) # turn it into an integer 
#    else:
#        dead("Man, learn to type a number.")        
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else: 
        dead("You greedy bastard!")
#%
def bear_room():
    print("There is a bear here.")
    print("The bear has bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True: # this actually loops untill on of the correct answer is provided
        # if choice is provided then it exists the while loop using one of 
        # functions - dead() or gold_room() :)))))
        choice = input("take honey or taunt bear or open door >>>")        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved: # only once allowed 
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True # sets to true and loops back 
        elif choice == "taunt bear" and bear_moved: # first you need to taunt bear then enter in
            dead("The bear gets pissed off and chews you")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "exit":
            print("yOU LOOSER exit - break")
            break
        else:
            print("I got no idea what that means")
#%
def cthulhu_room():
    print("Here you can see the great evil Cthulhu.")
    print("He, its, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head?")    
    choice = input("flee or head >>> \t")    
    if "flee" in choice: 
        # looks like that python uses in for == 
        # therefore this checks if "flee" is equal to choice
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else: 
        cthulhu_room()        
def dead(why):
    print(why,"Good job!")
    exit(0) # Exit the interpreter by raising SystemExit(status)    
#%%
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("left or right >>> ")    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "exit":
        dead("you LOOSER exit")
    else:
        dead("You stumble around the room until you starve")
#%% this function actually starts first 
start()      