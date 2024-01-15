import random as r

# Function to play the word guessing game for a given difficulty level
def guess(x):
    n = 0
    with open(f"{x}.txt", "r") as e:  # Open and read the file for the chosen difficulty level
        file = e.read().split(",")  # Split the words in the file using commas as separators

    for i in range(5):  # Play 5 rounds
        lst = []
        word = r.choice(file).strip()  # Choose a random word from the file
        for letter in word:
            lst.append(letter)

        print(f"{i+1}: ", end="")  # Print the round number

        for j in r.shuffle(lst):  # Shuffle the letters in the word
            print(j, end="")  # Print the shuffled letters

        if input('\nEnter your guess: ') == word:  # Get user input for the guessed word
            print("Correct Answer.\n")
            n += 1  # Increment the score for correct guesses
        else:
            print(f"Wrong, The answer was {word}\n")  # Display the correct answer if the guess is wrong

    return n  # Return the score for the difficulty level

# Function to start the word guessing game
def start():
    dict_ = {
        "easy": 0,
        "medium": 0,
        "hard": 0
    }
    n = 0
    name = input("Enter your Name: ")  # Get the player's name
    print(f"\nWelcome {name} to the Word Guessing game")

    while True:
        print("Select your Level:\n1. Easy\n2. Medium\n3. hard\n4. Exit")
        choice = input('\nChoose your option(1-4): ')

        if choice == '1' or choice.lower() == 'easy':  # Check if the player selected easy level
            dict_["easy"] += guess("easy")  # Play the game for easy level and update the score
        elif choice == '2' or choice.lower() == 'medium':  # Check if the player selected medium level
            dict_["medium"] += guess("medium")  # Play the game for medium level and update the score
        elif choice == '3' or choice.lower() == 'hard':  # Check if the player selected hard level
            dict_["hard"] += guess("hard")  # Play the game for hard level and update the score
        elif choice == '4' or choice.lower() == 'exit':  # Check if the player chose to exit
            print("\nScore Board")
            for i, j in dict_.items():
                print(f"{i}:{j}")  # Display the final scores
            print("\nSuccessfully Exited from the Game...\n")
            quit()  # Exit the program
        else:
            print("\nInvalid Choice...\n")  # Display an error message for invalid choices

start()  # Start the game
