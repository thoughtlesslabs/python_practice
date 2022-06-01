average_name_length = 12

# User inputs first name
first_name = input("What is your first name? ").strip().capitalize()

# User inputs last name
last_name = input("What is your last name? ").strip().capitalize()

# Saves length of first and last name
name_length = len(first_name) + len(last_name)

# Compares total length to average length and prints
if name_length == average_name_length:
    print(
        f"Your name, {first_name} {last_name} is the same length as the average name")
elif name_length > average_name_length:
    print(
        f"Your name, {first_name} {last_name} is longer than the average name")
elif name_length < average_name_length:
    print(
        f"Your name, {first_name} {last_name} is shorter than the average name")
