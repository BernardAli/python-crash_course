cars = ["nissan", "daewoo", "ford", "honda", "toyota", "mazda"]
print(cars[0])
print(cars[-1])
print(cars)

print(f"I wish to own 2021 {cars[4].title()} car next year")
cars[1] = "subaru"

print(cars)
cars.append('mitsuibishi')
print(cars)
cars.insert(0, 'audi')
print(cars)

# Remove
cars.pop()
print(cars)

cars.remove('audi')
print(cars)

del cars[0]
print(cars)

# sorting
cars.sort()
print(cars)

# reverse
cars.sort(reverse=True)
print(cars)