cars = ["nissan", "kia", "honda", "mazda", "audi", "vw", "bmw", "benz", 'daewoo']
print(cars)
print(len(cars))

print(cars[0])
print(cars[3])
print(cars[-1])

print(f"I would like to buy {cars[0].title()} by end of this year")

# changing values in a list
cars[-1] = 'GMC'
print(cars)

# Add -insert, append
cars.insert(0, 'toyota')
cars.append(['mitsuibishi', 'fiat'])
print(cars)

# changing values
cars[4] = "ford"
print(f"I would like to try the {cars[5]} lightning pickup next year")
print(cars)

# removing - remove, del, pop
del cars[-1]
cars.remove('kia')
print(cars)
cars.pop(1)
print(cars)

# Organizing
sort_cars = sorted(cars)
print(sort_cars)
print(cars)

# Permanent Sorting (sort, reverse)
cars.sort(reverse=True)
print(cars)
print(len(cars))
