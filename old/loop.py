message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Loop
# while
number = 0
while(number <= 10):
    print(number)
    number += 1

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)