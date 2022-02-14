# Shawn_Stock_Challengegit 
print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
client_name = input('What is your name? ')
# TODO: Write code to ask the client his savings and save it to another variable.
client_savings = input('What are your savings? ')
input = int(input('What are your savings? '))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:
if stock == "amzn":
    ...
elif ...
else ...
'''
if stock == 'amzn':
    price = amazon
    shares = client_savings/price
elif stock == 'aapl':
     price = apple
     shares = client_savings/price
elif stock == 'fb':
     price = fb
     shares = client_savings/price
elif stock == 'goog':
     price = google
     shares = client_savings/price
elif stock == 'msft':
     price = msft
     shares = client_savings/price
else:
    print('Sorry, insuffient funds')

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
print(f"{client_name} has {client_savings} in savings and they can buy {shares} shares of {stock} at the current price of {price}")

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print() 