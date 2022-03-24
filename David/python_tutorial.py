#python_tutoria
'''
class Restaraunt:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaruant(self):
        print(f'{self.name} serves {self.cuisine}.')
            
    def open(self):
        print(f'{self.name} is open')

rest1 = Restaraunt('Dyvine', 'BBQ')
rest1.open()
rest1.describe_restaruant()

rest2 = Restaraunt('Joe', 'Dogs')
rest3 = Restaraunt('Dunkin Donuts', 'Donuts')

rest2.open()
rest2.describe_restaruant()

rest3.open()
rest3.describe_restaruant()
'''

class Car:
    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")    

    def update_odometer(self, mileage):
        self.odometer_reading = mileage    

class Electric_car(Car):
    def __init__(self, make, model, year):     
        super().__init__(make, model, year)  
        self.battery_size = 75

    def describe_battery(self):
        print(f'My Tesla has a {self.battery_size} Volt battery.')

my_tesla = Electric_car('tesla', 'model S', 2009)    
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_new_car = Car('BMW', '325i', '2003')
my_new_car.odometer_reading = 23
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


