#print(David_restuarant_challenge)

#print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp.
Go through the dictionary and print out the following 3 pieces of information about the restaurant:
1. The latitude and longitude of Four Barrel Coffee
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
#print(f'The latitude and longitutde for {[name]} is {[latitude]} and {[longitude]}')
print(restaurant ["latitude"])
print(restaurant ['longitude'])

# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print(restaurant ['name'], restaurant ['address1'], restaurant ['city'], restaurant ['state'], restaurant ['zip_code'])

# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(restaurant ['url'])




print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
  #1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)
# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this

restaurant_1 = {
    "name": "Mission Bbq",
    "address": "1234 My Street, Dumfries, VA 22025",
    "favorite_dish": "Pulled Pork Sandwich",
}      

restaurant_2  = {
    "name": "Le Sur la Tab",
    "address" : "5th & Main, NY 10016",
    "favourite_dish" : "Stuffed Ant Legs",
}

restaurant_3 = {
    "name": "Caraba",
    "address": "7893 Minnieville Rd, VA 22193",
    "favourite_dish": "Chicken Bryan",
}

print(restaurant_1)
print(restaurant_2)
print(restaurant_3)


print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there.
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

print()

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address.
Update just this value in that restaurant's dictionary
'''

restaurant_1.pop('favorite_dish')
print(restaurant_1)



# TODO: Update the address field of 1 restaurant
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.

restaurant_2['address'] = "223 Peace Ct, Montclair, VA 22038"
print(restaurant_2['address'])

print("Question 5")
'''
Printing out all 3 of our restaurants every time is getting annoying. Let's clean up our code!
'''

# TODO: Put your 3 restaurant dictionaries into a list called `restaurants`
# TODO: Loop through your list and print out the name and address of each restaurant

reataurants = [restaurant_1, restaurant_2, restaurant_3]
for restaurant in reataurants:
    print(restaurant['name'])
    print(restaurant['address'])