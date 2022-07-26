class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
    # """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class Car:
    def __init__(self, make, model, year, odometer_reading = 0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        return f'{self.year} {self.make} {self.model}'

    def read_odometer(self):
        print(f"This {self.model} has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


# Inheritance

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    # def describe_battery(self):
    #     print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")