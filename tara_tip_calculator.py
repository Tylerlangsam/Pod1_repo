# welcomes user 
print(' Welcome to the tip calculator')

# variable of bill that will print message allowing the user to input amount
bill = float(input(' Please enter total of bill: '))

# varialbe of tip that allows user to imput amount desired
tip = float(input(' Please enter tip percent: '))

# variable of pepole that allows user imput
num_pepole = int(input(' How many pepole will be paying?:'))


print('\n')

# this will do math to round out the number of guests, tip, bill and adding a 10% tax
total_per_person = ('%.1f' % round(float(((tip / 100 +1)* bill) / num_pepole), 3))
 
tip = "%.1f" % float(tip / 100 * bill)
print(f'tip: ${tip}')



# created new variables in order to give the individual total of bill with tax and tip
bill_float = float(bill)
tip_float = float(tip)
tip_and_bill = (bill_float + tip_float)
print(f'total including tip: ${tip_and_bill}')


seprate_checks = round(tip_and_bill / num_pepole,3)
print(f' You each will pay: ${seprate_checks}')

