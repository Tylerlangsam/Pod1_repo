print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amzn = 3000
aapl = 100
fb = 250
goog = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input( "enter your name?")
print(name)


# TODO: Write code to ask the client his savings and save it to another variable.
savings = input("enter your savings")
print(savings)
x = int(savings)
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.

stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print(stock)

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
stockamount = 0
stockname = ''
stockprice = 0
if stock == "amzn":
    stockname = "amazon"
    stockamount = x / amzn
    stockprice = amzn
    print(stockamount)
elif stock == "aapl":
    stockname = "apple"
    stockamount = x / aapl
    stockprice = aapl
    print(stockamount )
elif stock == "fb":
    stockname = "facebook"
    stockamount = x / fb
    stockprice = fb
    print(stockamount)
elif stock == "goog":
    stockname = "google"
    stockamount = x /goog
    stockprice = goog
    print(stockamount)
else:
    print('line40')


'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
# amazon = 3000
# apple = 100
# fb = 250
# google = 1400
# msft = 200
# print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
print(f'{name} has {x} in savings and he can buy {stockamount} of {stockname} at the current price of{stockprice}')