print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200


# ask the client his name and save it to a variable.
client_name = input('Please enter your name: ')

# ask the client his savings and save it to another variable.
client_savings = int(input('Please enter your savings amount: '))

# ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft: ")
while stock != 'amazon' and stock != 'aapl' and stock != 'fb' and stock != 'google' and stock != 'msft':
    print(f"\nERROR: {stock} is invalid.")
    stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft: ")    
print()

# find out the number of stocks of the company that can be purchased with the savings amount.
if stock == 'amzn':
    shares = client_savings/amazon
elif stock == 'aapl':
    shares = client_savings/apple
elif stock == 'fb':
    shares = client_savings/fb
elif stock == 'goog':
    shares = client_savings/google
elif stock == 'msft':
    shares = client_savings/msft


print()

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print(f"{client_name} has {client_savings} in savings and can buy {int(shares)} shares of {stock}")
