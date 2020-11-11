print('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888  
''')

print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    'You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if choice1 == "left":
    choice2 = input(
        '\n\nYou\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input(
            "\n\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("\n\nIt's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("\n\nYou found the treasure! You Win!")
        elif choice3 == "blue":
            print("\n\nYou enter a room of beasts. Game Over.")
        else:
            print("\n\nYou chose a door that doesn't exist. Game Over.")
    else:
        print("\n\nYou get attacked by an angry trout. Game Over.")
else:
    print("\n\nYou fell into a hole. Game Over.")
