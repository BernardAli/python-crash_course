from traceback import print_last

message = "Hello Ben"
print(message)

# Strings
name = "Bernard Ali "
print(f"My name is {name}")
print(f"My name is {name.upper()}")
print(len(name))
name = name.strip()
print(f"My name is {name.upper().strip()}")
print(len(name))

# Numbers
# float, integers
print(2 ** 9)
print(2.000001 + 9)


# Large numbers
world_population = 7_900_000
print(world_population)

# Multiple assignment
a, b, c = 12, 13, 14
print(a)

# Constants
# Use upper case for constants
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

import this