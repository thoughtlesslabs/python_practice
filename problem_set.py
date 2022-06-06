#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# # Write a for loop that prints out each character in the above "word" variable
# for i in word:
#     print(i)

# Write a while loop that does the same thing!
i = 0
while i < len(word):
    print(word[i])
    i += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
i = 100
while i < 141:
    print(i)
    i += 2

# Write a for loop that does the same thing (with range())
for i in range(100, 141, 2):
    print(i)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
user_input = input("Write sillygoose ")
while user_input != "sillygoose":
    user_input = input("Write sillygoose ")
    print("Not sillygoose")

print('You are a sillygoose')
