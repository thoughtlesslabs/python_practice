for i in range(99, 0, -1):
    bottle_grammar = f"{i} bottles"
    last_line = f"{i-1} bottles"
    if i == 2:
        last_line = f"{i-1} bottle"
    elif i == 1:
        bottle_grammar = f"{i} bottle"
        last_line = "No more bottles"

    print(bottle_grammar + ' of beer on the wall')
    print(bottle_grammar + ' bottles of beer!')
    print("Take one down, pass it around.")
    print(last_line + " of beer on the wall")
    print("**********************************************")
