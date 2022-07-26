import random

cars = ["nissan", "kia", "honda", "mazda", "audi", "vw", "bmw", "benz"]

# looping
for car in cars:
    print(car.title())
print('Thanks for checking our cars out')


# Numerical list with range
numbers = range(0, 11, 1)
print(list(numbers))

for num in numbers:
    print(num)

square = [x ** 2 for x in numbers]
print(square)
print(sum(numbers))

# random
rand_values = random.randint(0, 10)
print(rand_values)

# working with part of the list
print(len(square))
print(square[2:])

upper_square = square[4:]
print(upper_square)
for value in upper_square:
    print(value, end=",")
print("\n")

# Copying lists

new_cars = cars.copy()
print(new_cars)
new_cars.append('hyundai')
cars.append('ram')
print(new_cars)
print(cars)


check = 'audi' in cars
print(check)

print(max(numbers))
print(min(numbers))
print(sum(square))