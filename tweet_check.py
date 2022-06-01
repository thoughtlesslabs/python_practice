max_length = 140

# Take user input of tweet
user_tweet = input("enter your tweet: ")

# Calculate the length of tweet
tweet_length = len(user_tweet)

# Check to make sure the tweet is less than 140 and print response
if tweet_length <= max_length:
    print(f"Your tweet is {tweet_length} characters long and will work!")
else:
    print(
        f"Your tweet is {tweet_length} characters and is {tweet_length - max_length} characters to long")
