# BONUS: Add AI
import random

# Get Player Names
player_one = input("What is your name? ")
player_two = input("What is your name? ")

# Game loop
# Choose starting player
# Ask how many toothpicks to remove
# Check to make sure number is 1,2,3
# Remove toothpicks from total
# Display remaining toothpicks
while True:
    toothpicks = 13
    active_player = random.randint(1, 2)-1
    player_table = [player_one, player_two]
    while toothpicks >= 1:
        print(" |" * toothpicks)
        choice = 4
        if active_player == 1:
            active_player = 0
        else:
            active_player = 1

        while choice > 3:
            choice = int(input(
                f"How many toothpicks would you like to remove {player_table[active_player]}? "))
            new_total = toothpicks - choice

            if new_total < 0 or choice > 3:
                print('Too many picks. Try a lower number')
                choice = 4

        toothpicks = new_total

    print(f"Congratulations {player_table[active_player]}! You win!")

    break


# No invalid responses of 1,2,3
