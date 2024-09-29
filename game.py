#mero ma aurko lina mildaina so maile auta auta import gare rakhnu parxa
import time
import random

#this one is for the display
#display garda sabbi 1 kaai choti vanda slowly aako ramro hunxa hola vane ra
def print_slowly(text, delay=0.05):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)
    print()


#yo chai hamro console clear garna lai after each print out but not in function
def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

#yo chai normal idea what to do after the challange is done vane ra
def challenge(challenge_text, reward):
    print_slowly(challenge_text)
    input("Press Enter to complete the challenge...")
    print_slowly(f"You have received: {reward}!")

#1st ma print hune wala yo chai like front page ma k auxa vane ra ani thyo paxi yo aafi delete hune banu ne
def adventure_game():
    clear_console()
    print_slowly("Welcome to the Adventure Game: The Treasure of Francis Drake!")

    print_slowly("You are a retired pilot...")
    print_slowly("One day you discover an old bottle by the sea shore with a map for hidden treasure...")

    input("Press Enter to start your journey from the first airport in China...") #airpot ko name needed

     #just yo chai normally k garne idea lena lai lekhya ko ho
    challenges = [
        ("Navigate through a stormy weather system to reach the next airport.", "Enhanced navigation tools."),
        ("Manage fuel levels while making your way to the next destination.",
         "Fuel efficiency upgrades for your aircraft."),
        ("Avoid pirate territories and navigate safely to Panama.", "Maps of safe routes.")
    ]

    for challenge_text, reward in challenges:
        challenge(challenge_text, reward)

    print_slowly("You have arrived at Panama Isthmus where the treasure is hidden!")
    print_slowly("Congratulations! You've discovered the hidden fortune and won the game!")

adventure_game()
