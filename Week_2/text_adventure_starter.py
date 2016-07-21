start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''
start_message = "Type 'left' to go left or 'right' to go right."
unrecognisable_input_Zeus_left_right = "That is not an answer. You think you hear something from above coming towards you. You must make a decision: left or right."
left_Zeus_offers_help = "You decide to go left and you encounter Zeus, who offers you his help to get out of the maze."
unrecognisable_input_Zeus_yes_no = "Zeus will not take that as an answer. He finds you an annoying mortal and contemplates killing you. He asks you once more if you want his help. Answer 'yes' or 'no'."

print("start")

print(start_message)
user_input = input()
while (user_input != "left" and user_input != "right"):
    print(unrecognisable_input_Zeus_left_right)
    user_input = input()

if user_input == "left":
    print(left_Zeus_offers_help)
    print("Do you take his help?")
    user_input = input()
    while (user_input != "yes" and user_input != "no"):
        print("Zeus will not take that as an answer. He finds you an annoying mortal and contemplates killing you. He asks you once more if you want his help. Answer 'yes' or 'no'.")
        user_input == input()
    
    if user_input == "yes":
        print("Zeus offers you two options. He can (a) fly you up above the maze walls to see what you are up for, or (b) he could provide you a lightning bolt after informing you of the dangers ahead.")
        user_input = input()
    if user_input == "a":
        print("Zeus flies you up, but then drops you and you die.")
        print("GAME OVER")
    if user_input == "b":
        print("You electrify  yourself when you touch the bolt and die.")
        print("GAME OVER")
    if user_input == "no":
        print("Zeus shrugs, claiming you'll die. But you eventually make if out of the maze and live.")
        print("GAME OVER")
elif user_input == "right":
    print("You choose to go right and you encounted Hades who offers you his help to get out of the maze.")
    print("Do you take his help?")
    user_input = input()
    if user_input != "yes" or "no":
        while user_input != ("yes" or "no"):
            print("Hades will not take that as an answer. He asks you again if you want his help. Answer 'yes' or 'no'.")
            user_input == input()
    if user_input == "yes":
        print("Hades offers you two options. He can (a) take you down to the underworld for a shortcut to the exit or (b) he can grant you the ability to walk through walls to get out of the maze.")
        user_input = input()
        if user_input != "a" or "b":
            print("Hades is starting to get frustrated with you. Choose option 'a' or 'b'.")
            user_input == input()
        if user_input == "a":
            print("Hades takes you down to the underworld and never lets you leave, which basically means your dead.")
            print("GAME OVER")
        if user_input == "b":
            print("You were granted the ability to walk through walls, but you end up falling through the ground into the underworld as Hades laughs at you. So you die.")
            print("GAME OVER")
    if user_input == "no":
        print ("Hades glares at you, but lets you pass (surprisingly) and observes as you make your way out of the maze and live.")
        print("GAME OVER")