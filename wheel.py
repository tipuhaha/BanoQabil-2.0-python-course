import random

def wheel_spin():
    print("WELCOME TO THE WHEEL!!! ")

def wheelbox():
    symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']

    # Display available symbols
    print("Available symbols: ", symbols)

    # Get user input for the bet
    user_bet = input("Place your bet on one of the symbols: ").capitalize()

    # Check if the user's bet is valid
    if user_bet not in symbols:
        print("Invalid bet. Please choose a valid symbol.")
        return
    
# Spin the wheel
    wheel_result = random.choice(symbols)
    print("Wheel spinning... Result: ", wheel_result)

    # Determine the outcome
    if user_bet == wheel_result:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Try again.")

# Run the wheelbox game
wheelbox()