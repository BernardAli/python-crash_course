cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'audi':
        print(f'This must be {car.title()} Q8')
    else:
        print(car.title())

var = not cars
print(var)

print("ben" == "ben")
print("ben" == "Ben")

print('ford' not in cars)


available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['salad', 'mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")