# print('1.1: Create a variable called `meal`, and save a string describing what you had for lunch in it')
meal= 'Chocolate chip cookies'

# print('1.2: Print the meal variable')
print(meal)

# print('1.3: Update the meal variable to be a string describing what you want for dinner. print it out again')
meal= 'meatloaf with extra gravy'
x= meal.replace("Chocolate chip cookies", "meatloaf with extra gravy")
print (x)

# print('2: How old is Google?')
Google_age=2022-1993
print(Google_age)
# 2.1: Google was founded in 1993. The current year is 2022. Create a variable called google_age, and use subraction
# to figure out how old Google is
# ex: my_age = current_year - birth_year


# 2.2: Print out a sentence about Google's age. Make sure to include your variable in the f-string!
y='Google age is'
New_sentence_about_Google_age= f"{y} {Google_age}"
print(New_sentence_about_Google_age) 


# 2.3 How many _months_ old is Google? Create a new variable google_age_months, and use multiplication to figure it out,
# then print the info.
# (Assume 12 months for each year, you don't need to check which month they started)
google_age_months='348 months old'
g='Google is'
New_sentence_about_Google_age_months=f"{g} {google_age_months}"
print(New_sentence_about_Google_age_months)

# print('3.1: The line of code below is commented out because it produces many SyntaxErrors.')
# print('Fix the problem and turn the comment back into regular Python code')
# completion message = ('Completed the first Python challenge!
completion_message= 'Completed the first Python challenge!'
print(completion_message)
# print('Completed the first Python challenge!')

# 3.2 What were the syntax errors that you fixed? print out a quick explanation of each one.
# completion message variable missing underscore. Apostrophe missing at end of !

# print('3.3: Turn the comment below back into regular Python code')
# print(completion_message)
print('completion_message')