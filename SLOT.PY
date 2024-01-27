import random

def spin_reels():
    symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']

    # Spin the reels and get random symbols for each reel
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    # Display the result
    print(f"Reel 1: {reel1} | Reel 2: {reel2} | Reel 3: {reel3}")

    # Return the symbols as a tuple
    return reel1, reel2, reel3

def check_winning(reels):
    # Check for winning combinations
    if reels[0] == reels[1] == reels[2]:
        return True
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return True
    else:
        return False

def slot_machine():
    print("Welcome to the Slot Machine!")

    # Main game loop
    while True:
        input("Press Enter to spin the reels...")

        # Spin the reels
        result = spin_reels()

        # Check for winning combination
        if check_winning(result):
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose. Try again.")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

# Run the slot machine game
slot_machine()
