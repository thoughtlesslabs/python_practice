# Another Rock Paper Scissor Game
# Let's see if I can do this any better
import random
# Image ASCII art
rock = '''
     __________
    /     _____/
----    (_____)
        (_____)
----    (_____)
    \___(_____)
'''

paper = '''
     __________
    /        __/______
----         _________)
             __________)
----         ________)
    \______________)
'''

scissors = '''
     __________
    /        __/______
----         _________)
             __________)
----     (____)
    \____(____)
'''

player_score = 0
ai_score = 0

# Game Loop
while True:
    # Get input from player (rock, paper, or scissors)
    # Display the result

    player_choice = input("enter your move: ").lower()
    if player_choice == 'rock':
        print(rock)
    elif player_choice == 'paper':
        print(paper)
    elif player_choice == 'scissors':
        print(scissors)
    else:
        print('Invalid selection. Try again')
        continue

    # AI player chooses rock, paper, or scissors
    # Display the result
    ai_choice = random.randint(1, 3)

    if ai_choice == 1:
        ai_choice = 'rock'
        print(rock)
    elif ai_choice == 2:
        ai_choice = 'paper'
        print(paper)
    else:
        ai_choice = 'scissors'
        print(scissors)

    print(ai_choice)
    # Evaluate who wins
    # Display winner

    if player_choice == ai_choice:
        print("It's a tie!")
    elif player_choice == 'rock' and ai_choice == 'scissors' or player_choice == 'paper' and ai_choice == 'rock' or player_choice == 'scissors' and ai_choice == 'paper':
        player_score += 1
        print("Player wins!")
    else:
        ai_score += 1
        print('Computer Wins!')

        print(f'''
Scores:
*********************

Player Score: {player_score}
Computer Score: {ai_score}

*********************
    ''')

    while True:
        new_game = input("Would you like to play again? ").lower()

        if new_game == "yes" or new_game == "y":
            start_new = True
            break
        elif new_game == "no" or new_game == "n":
            start_new = False
            break
        else:
            print("Invalid response. Please enter (y/yes or n/no)")
            continue
    if start_new:
        continue
    else:
        break
print('Thanks for playing!')
