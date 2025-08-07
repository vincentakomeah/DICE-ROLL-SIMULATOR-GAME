# Import the random module to enable random selections
import random

# Display the game title
print("DICE ROLL SIMULATOR GAME")

# Define possible dice face values as strings
numbers = ['1', '2', '3', '4', '5', '6']

# Define dice visuals corresponding to each number
dices = [
    '🎲',
    '🎲🎲',
    '🎲🎲🎲',
    '🎲🎲🎲🎲',
    '🎲🎲🎲🎲🎲',
    '🎲🎲🎲🎲🎲🎲',
]

# Initialize the player's score
score = 0

# Start the game loop
while True:
    # Prompt the user to input a number between 1 and 6 or 'q' to quit
    user_play = input("\nEnter a number from 1 to 6 to roll the dice ('q' to quit): \n")

    # Randomly select a number for the computer's play
    computer_play = random.choice(numbers)

    # If the user wants to quit, confirm their decision
    if user_play == 'q':
        exit_query = input("Are you sure you want to quit? Enter either 'yes' or 'no': ").lower()
        if exit_query == 'yes':
            print("\nAww BYE! Let's play again later, okay👋.\n")
            break
        else:
            print("\nWow COOL! Let's play then🤗.\n")
            continue

    # Handle invalid entries that are not between 1 and 6
    if user_play not in numbers:
        print("Wrong entry. Please enter a number from 1 to 6.😵‍💫")
        continue

    # Check if the user's guess matches the computer's roll
    if user_play == computer_play:
        # Print the corresponding dice visual
        print(dices[int(computer_play) - 1])

        # Notify the user of their win and update score
        print("YOU WIN 😁😁😁")
        score += 1
        print(f"SCORE: {score}")
    else:
        # Print the corresponding dice visual even when user loses
        print(dices[int(computer_play) - 1])

        # Notify the user of their loss and update score
        print(f"Computer_play: {computer_play}")
        print("YOU LOOSE 🥶🥶🥶")
        score -= 1
        print(f"SCORE: {score}")
