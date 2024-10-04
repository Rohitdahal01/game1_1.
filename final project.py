import time
import os
import random


# console clear function
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# text slow define function
def print_slowly(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to next line


# Plane take off
def print_airplane():
    airplane = """
         __|__
  --@--@--(_)--@--@--  
           """
    print(airplane)


# plane crash
def print_airplane_crash():
    crash = """
           __|__
  --@--@--(_)--@--@--
    \______/  \____/
     (O)(O)   (X)(X)
     Plane Crash!
    """
    print(crash)


# Get user's age
def get_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            return age
        except ValueError:
            print("Invalid input. Please enter a valid age.")


# Challenges based on age
def get_challenges_from_db(age):
    if age < 12:
        return [
            ("What is 5 + 3?", "8", "It's a simple math addition."),
            ("What color is the sky on a clear day?", "blue", "Look up and you will see."),
            ("What sound does a dog make?", "bark", "Think of a common pet's sound.")
        ]
    else:
        return [
            (
            "You find a locked door with a riddle: 'I speak without a mouth and hear without ears. What am I?'", "echo",
            "It's something you can hear in a canyon."),
            (
            "A code to unlock the treasure chest says '4 legs in the morning, 2 at noon, and 3 in the evening.' What is it referring to?",
            "human", "Think of the stages of life."),
            ("Solve this anagram: 'hetreusa', which leads to the treasure.", "treasure",
             "Rearrange the letters to find your reward.")
        ]


# Plane take off sequence
def airplane_sequence():
    clear_console()  # Clear console for a clean look
    print_airplane()  # Show airplane
    # Prompt for takeoff
    while True:
        user_input = input("You are in the airplane. To take off, press 't': ").strip().lower()
        if user_input == 't':
            print_slowly("The plane is ready, but you need to complete some challenges before it can take off...\n")
            return True
        else:
            print_slowly("Incorrect key! The plane will crash!\n")
            print_airplane_crash()  # Show crash airplane
            return False  # Crash and restart


# Handle the first challenge with two attempts
def handle_first_challenge(challenge_text, answer, hint):
    attempts = 2
    for attempt in range(attempts):
        user_answer = input(f"{challenge_text}\nYour Answer: ").strip().lower()
        if user_answer == answer.lower():
            print_slowly("Correct! You solved the challenge!\n")
            return True
        else:
            if attempt == 0:
                print_slowly("Incorrect. You have one more try.")
            else:
                print_slowly("Incorrect again. Here's a hint:\n")
                options = generate_multiple_choice(answer)  # Generate options with the correct answer included
                print_slowly(f"Hint: {hint}")
                for idx, option in enumerate(options, 1):
                    print(f"{idx}. {option}")
                try:
                    choice = int(input("Choose the correct option (1-4): "))
                    if options[choice - 1].lower() == answer.lower():
                        print_slowly("Correct! You solved the challenge!\n")
                        return True
                    else:
                        print_slowly("Incorrect again. Game Over! Restarting...\n")
                        return False
                except (ValueError, IndexError):
                    print_slowly("Invalid choice. Game Over! Restarting...\n")
                    return False
    return False


# Generate multiple choice options for a question
def generate_multiple_choice(correct_answer):
    wrong_answers = ["apple", "moon", "car", "water"]
    wrong_answers = [ans for ans in wrong_answers if ans.lower() != correct_answer.lower()]
    options = random.sample(wrong_answers, 3) + [correct_answer]
    random.shuffle(options)
    return options


# Handle other challenges with no attempts
def handle_challenge(challenge_text, answer):
    user_answer = input(f"{challenge_text}\nYour Answer: ").strip().lower()
    if user_answer == answer.lower():
        print_slowly("Correct! You solved the challenge!\n")
        return True
    else:
        print_slowly("Incorrect. Returning to the last challenge you completed.\n")
        return False


# Random question for Melbourne
def random_melbourne_question():
    return "What is the capital of Australia?", "canberra"


# Antarctica landing sequence
def antarctica_landing_sequence():
    clear_console()
    print_slowly("WARNING! You are about to land at Novo Airbase, Antarctica...\n")
    print_slowly("The runway is snowy and slippery, please be careful!\n")

    # Random keys for landing (more than 5)
    keys = "abcdefghijklmnopqrstuvwxyz"  # You can include more characters if you want
    random_keys = random.sample(keys, 6)  # Change the number to increase the keys
    random_key = random.choice(random_keys)

    print(f"To land safely, press one of these keys within 3 seconds: {', '.join(random_keys)}...\n")

    start_time = time.time()
    user_input = input().strip().lower()
    time_taken = time.time() - start_time

    if user_input in random_keys and time_taken <= 3:
        print_slowly("Phew! You've landed safely at Novo Airbase, Antarctica!\n")
    else:
        print_slowly("Oh no! You didn't press the key in time. The plane crashed!\n")
        print_airplane_crash()
        return False  # Return False to indicate failure
    return True  # Return True for successful landing


# Main game function
def adventure_game():
    clear_console()

    # Display the story first
    print_slowly("Welcome to the Adventure Game: The Treasure of Francis Drake!\n")
    print_slowly("You are a retired pilot...\n")
    print_slowly("One day, you discover an old bottle by the seashore with a map for hidden treasure...\n")
    input("You are at Chengdu Huangtianba AirBase... (Press Enter to continue)\n")

    # Ask for the age
    age = get_age()

    # Airplane takeoff sequence logic, requires challenges to be solved
    if not airplane_sequence():
        return  # Plane crashes, restart

    # Retrieve challenges based on age
    challenges = get_challenges_from_db(age)

    # First challenge has 2 attempts
    first_challenge_text, first_answer, first_hint = challenges[0]
    if not handle_first_challenge(first_challenge_text, first_answer, first_hint):
        return  # Game over, restart

    # Plane takes off and lands at Melbourne
    print_slowly("Congratulations! You have taken off and landed safely at Melbourne, Australia.\n")
    print_slowly("However, to take off again, you need to answer a question.\n")

    # Melbourne task (random question)
    melbourne_question, melbourne_answer = random_melbourne_question()
    if not handle_challenge(melbourne_question, melbourne_answer):
        return  # Restart if the question is wrong

    # Antarctica landing sequence
    print_slowly("You are now flying toward Novo Airbase, Antarctica...\n")
    if not antarctica_landing_sequence():
        # Redirect back to the first challenge if the player fails to land
        print_slowly("Redirecting you back to the first challenge...\n")
        if not handle_first_challenge(first_challenge_text, first_answer, first_hint):
            return  # Game over if they fail again

    # Ending
    print_slowly("Congratulations! You've successfully completed the game and reached the hidden treasure!\n")


# Main entry point
if __name__ == "__main__":
    adventure_game()
user_input = input(printf("What is your name"))
printf("welcome ")