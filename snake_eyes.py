# Roll two dice and keep rolling until snake eyes
from random import randint as roll
import os
import time

os.system('clear')

dice_drawing = {
    1: '''
 ____________
|            |
|            |
|      x     |
|            |
|____________|
''',
    2: '''
 ____________
|            |
|   x        |
|            |
|        x   |
|____________|
''',
    3: '''
 ____________
|            |
|   x        |
|     x      |
|        x   |
|____________|
''',
    4: '''
 ____________
|            |
|   x    x   |
|            |
|   x    x   |
|____________|
''',
    5: '''
 ____________
|            |
|   x    x   |
|      x     |
|   x    x   |
|____________|
''',
    6: '''
 ____________
|            |
|   x    x   |
|   x    x   |
|   x    x   |
|____________|
'''}

roll_count = 0

while True:
    die_one = roll(1, 6)
    die_two = roll(1, 6)

    print(f'''
You rolled a {die_one} and a {die_two}
{dice_drawing[die_one]}  {dice_drawing[die_two]}
    ''')

    if die_one == 1 and die_two == 1:
        print("Snake eyes!")
        print(f'It took you {roll_count} roll(s) to get snake eyes')
        break
    else:
        time.sleep(2)
        os.system('clear')
        roll_count += 1
        continue
