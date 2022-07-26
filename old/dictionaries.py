from more_itertools import value_chain


person = {
    'name': 'Ben',
    'age': 29,
    'address': {
        'city': 'Kumasi',
        'street': 'Cool Base'
    }
}

person['height'] = 182

del person['age']

print(person)
print(person['name'])

print(person.get('name', 'No name found'))

for per, value in person.items():
    print(per.upper(), value)
