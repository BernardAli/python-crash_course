from numpy import number


cars = ["nissan", "daewoo", "ford", "honda", "toyota", "mazda"]
for car in cars:
    print(f"i love {car.title()}")


# Range
numbers = range(1, 10)
for num in numbers:
    print(num ** 3)

nums = list(range(0, 10))
print(nums)

cube = [x ** 3 for x in nums]
print(cube)
print(len(cube))
print(cube[0:3])
print(cube[0:])
print(cube[:3])

cub = cube.copy()
print(cub)


# Tuples
dimensions = (200, 50)
dimensions = (100, 20)
print(dimensions[0])
print(dimensions[1])
