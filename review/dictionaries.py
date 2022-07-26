person = {'name': "Ben", 'age': 30}

person['address'] = {
    'town': 'Kumasi',
    'street': '123 st.',
}
person['interests'] = ['soccer', 'movie', 'outing']
print(person)

print(person['address'])
print(person['interests'][-1])
print(person)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, f'-> {value}')


aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens[:5])
print("...")
print(f'Total aliens are {len(aliens)}')


