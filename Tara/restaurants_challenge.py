print("Challenge: Favourite Restaurants")

print()

print("Question 1")

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
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(f'latitude is {restaurant["latitude"]}')
print(f'longitude is {restaurant["longitude"]}')
print(f'complete address is {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]}, {restaurant["zip_code"]}')
print(f'website is {restaurant["url"]}')



print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this
'''
'''

restaurant_1 = {
    "name": "Cucina Sorella",
    "address" : "4055 Adams Ave, San Diego, CA 92116",
    "favourite_dish" : "Gnocchetti Sardi"


}

restaurant_2 = {
    "name": "The Grill",
    "address" : "1092 E River RD, Pray, MT 59065",
    "favourite_dish" : "Chef Tasting Menu"



}

restaurant_3 = {
    "name": "Felix",
    "address" : "1023 Abott Kinney Blv, Venice, CA 90291",
    "favourite_dish" : "EVERYTHING!"


}
print(restaurant_1)
print(restaurant_2)
print(restaurant_3)
'''





'''
print()

print("Question 3")

#Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there.
# Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
'''
restaurant_1.pop('favourite_dish')
print(restaurant_1)
print()

print("Question 4")


# Imagine that another one of your most favourite restaurants modified its address.
# update just this value in that restaurant's dictionary


# TODO: Update the address field of 1 restaurant
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.
restaurant_2["address"] = '103 S 9th st, MT 59047'
print(restaurant_2)
print()


print("Question 5")
#Printing out all 3 of our restaurants every time is getting annoying. Let's clean up our code!
# TODO: Put your 3 restaurant dictionaries into a list called `restaurants`
# TODO: Loop through your list and print out the name and address of each restaurant
restaurants = [restaurant_1,restaurant_2,restaurant_3]
print(restaurants)

for restaurant in restaurants:
    print(restaurant["name"],restaurant["address"])