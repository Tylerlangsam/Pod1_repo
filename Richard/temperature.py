
#Convert a temperature of 100 degrees fahrenheit to celsius
celsius_100 = (100-32)*5/9
print(f'100 degrees fahrenheit is {celsius_100} degrees celsius')

#Convert a temperature of 0 degrees fahrenheit to celsius
celsius_0 = (0-32)*5/9
print(f'0 degrees fahrenheit is {celsius_0} degrees celsius')

#Convert a temperature of 34.2 degrees fahrenheit to celsius
#Do this one all in one print statement without saving any variables
print(f'celsius 34.2 is {(34.2-32)*5/9} degrees fahrenheit')

#Convert a temperature of 5 degrees celsius to fahrenheit?
fahrenheit_5 = (5*9/5)+32
print(f'5 degrees celsius is {fahrenheit_5} degrees fahrenheit')

#What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
fahrenheit_30_2 = (30.2*9/5)+32
print(f'30.2 degrees celsius is {fahrenheit_30_2} degrees fahrenheit')
if fahrenheit_30_2 > 85.1:
    print('30.2 degrees celsius is hotter than 85.1 degrees fahrenheit')
else:
    print('85.1 degrees fahrenheit is hotter than 30.2 degrees celsius')
