from classes import Dog
from car import Car, ElectricCar, Battery

first_dog = Dog('defender', 2)
print(first_dog.name.title())
first_dog.roll_over()

first_car = Car('toyota', 'camry', '2001')
# first_car.odometer_reading = 23
first_car.update_odometer(56000)
first_car.increment_odometer(6000)
print(first_car.make.title())
print(first_car.get_descriptive_name())
first_car.read_odometer()   

tesla = ElectricCar('Tesla', 'Model S Plaid', 2022)
print(tesla.model)
print(tesla.get_descriptive_name())
tesla.read_odometer()
tesla.battery.battery_size = 100
tesla.battery.describe_battery()
tesla.battery.get_range()
