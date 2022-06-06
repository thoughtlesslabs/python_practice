import random


def player_input():
    # Ask user how many dice
    num_dice = int(input("how many dice? "))
    # Ask user how many sides are on the dice
    dice_side = 21

    while dice_side > 20:
        dice_side = int(input("how many sides? "))

    return num_dice, dice_side


player_choice = player_input()

while True:
    rolls = "|"

    for i in range(player_choice[0]):
        roll_die = random.randint(1, player_choice[1])
        rolls += f" {roll_die} |"

    print(rolls)

    play_again = input("Would you like to play again (y/n)? ")

    if play_again == "y":
        same_rolls = input("Would you like to change your dice? ")
        if same_rolls == 'y':
            player_choice = player_input()
        continue
    else:
        break

print("Thanks for playing!")
