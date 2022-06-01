print("Welcome to the Useless Store!")
print("*" * 30)
user_item = input("What would you like to purchase? ")
user_price = float(input(f"What is the price of {user_item}(s)? "))
user_qty = float(input(f"How many {user_item}(s) would you like to buy? "))

print(f"\nAdded {int(user_qty)} {user_item}(s) to the cart")
print(f"Subtotal: ${user_price * user_qty}")
