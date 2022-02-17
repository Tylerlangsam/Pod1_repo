# Week 3 Loops challenge 
# Pod 1
# Chris Kazas
# 2-16-22

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# 1.1: Write a for loop that prints out each day in the `days` variable above.
for day in days:
    print(day)


# 1.2: Now, instead of printing out the day, let's ask the user what their favorite thing
# to do is on that day of the week. (Make sure to use an f-string so that the user knows which
# day they're being asked about.)

# 1.3: We should keep track of the user's favorite things to do so that we can print them out all together.
# ABOVE your for loop, create a new empty list to hold the user's favorite activities.

# 1.4: Now, back in your for loop, append each of the user's answers into your new list.
# Print out the list after your loop to check if it got populated correctly.
activities = []
for day in days:
    activity = input(f"what is your favorite thing to do on {day}")
    activities.append(activity)
    


# 1.5: After your first loop, let's create a new one. As an example, let's say the user's favorite thing to
# do on mondays is plan their week. This time, we want the output to be something like this:
# 'On Mondays, your favorite activity is to plan your week.'
# We need information from both lists! Let's use the `range` function to loop through the indexes
# of the items in the lists (this will work because the lists are the same length).
# Each time through this new loop, use the index number to index into each of your lists for the data
# you need to print out.
for i in range(len(days)):
    print(f"On {days[i]}, your favorite activity is to {activity[i]}.")
    
# Write a program that loops through the days in the week. Each day, ask the user what the temperature
# is. If the temperature is below 50, tell the user to put on a jacket. Or, if the temperature is
# between 50 and 65, tell the user to put on a sweater. Finally, if the temperature is above 65,
# tell the user to put on some sunscreen.
for day in days:
    temperature = int(input(f"What is the temperature on {day}"))
    if temperature < 50:
        print('Please put on a coat')
    elif temperature >= 50 and temperature <= 65:
        print(f"Put on a sweater")
    else:
        print('Put on some sunscreen')

# ask the user what temperature it is outside. While the temperature is below 65,
# tell the user to wear a sweater. Once the temperature is over 65, stop looping, and tell the user that
# Spring has sprung!
temp = 0
while temp < 66:
    temp = int(input('What is the current temperature outside: '))
    
print('Spring has sprung!')