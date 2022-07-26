def greet():
    print("Hello Ben")

greet()

def greet(name):
    print(f"Hello {name}")

greet('Eddie')

def power(a, b):
    return a ** b

print(power(2, 4))
print(power(b=2, a=8))

# Passing a List
def greet_users(names):
# """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

greet_users(['ben', 'eddie'])
