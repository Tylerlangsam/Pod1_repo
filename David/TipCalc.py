print("Welcome to David Stevens' Tip Calculator") #Welcome the user to my program
pretax = float(input("Enter Pre-tax total "))#Enter the pretax total and convert to float
tax = float(pretax * .1) # The pretax amount times the tax, tax calculated at 10%
Total_bill_with_tax = float(pretax + tax)  #The total amount of the bill with tax included
tippercent = float(input("Enter tip percentage as a decimal "))#enter the tip in decimal form and convert to float
change_tip = print(input('Do you want to change the tip amount? y if yes and n if no: ' ))
if 'y': 
    f'{tippercent}'
totaltip = float(pretax * tippercent) #multiply pretax amount and tip convert to float 
#


numberoftippers = float(input("Enter number of Tippers "))#enter number of people tipping
tip = float(totaltip / numberoftippers)#divide total number of tip by the number of people tipping convert to float
print("Tip amount for each person $", round(tip, 2)) #print the tip amount for each person rounded to two decimal places
tipplustotal = float(Total_bill_with_tax / numberoftippers + tip)#print the total amount each person owes rounded to two decimal places 
print("Total each person has to pay $", round(tipplustotal, 2)) 