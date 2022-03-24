#Functions_pracice.py
'''
def Hi():
    print('Hello Everyone')
Hi()


if 46<5:
    Hi()
#print('Bye')


def Hiya(name):
    print(f'{name}')
    Hi()

Hiya('dave')
'''
'''
def icecream (flavor = 'chocolate'):
    print(f'{flavor} ice cream with hot fudge')
#icecream()
#icecream('Vanilla')

def name(firstname, middlename, lastname):
    print(f'Hello, {firstname} {middlename} {lastname}!')
name(firstname='Martin', middlename='Luther', lastname ='King')
'''

import os

#os.system('dir')
day_per_week = 7
#variables : Data
#functions : code

# say hello to the user
# tell the user my name
# tel the user to have a good day

def times_two(num):
    print(num * 2)

times_two(3)
times_two(4.0)

def multiply (a, b):
    return a * b

multiply(3, 5)
print(multiply)