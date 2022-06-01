unit = input("What unit are you using to measure (C/F/K)? ").lower()
temp = int(input("What is the current temperature? "))

if unit == "f":
    if temp >= 212:
        print("Your water is boiling!")
    else:
        print("Your water is not boiling")
elif unit == "c":
    if temp >= 100:
        print("Your water is boiling!")
    else:
        print("Your water is not boiling")
elif unit == "k":
    if temp >= 383:
        print("Your water is boiling!")
    else:
        print("Your water is not boiling")
