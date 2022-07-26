def greeting(name):
    print(f"Welcome {name.title()}")

name = input("Pls enter your name")
greeting(name)

def describe_self(first_name, last_name, second_name=''):
    if second_name:
        return f'My name is {first_name} {second_name} {last_name}'
    else: 
        return f'My name is {first_name} {last_name}'

me = describe_self('Ben', 'Ali')
print(me)

# return a dictionary
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

him = build_person('solomon', 'billa', 28)
print(him)


def sqaures(numbers):
    return [x ** 2 for x in numbers]

numbers = [1, 2, 3, 4, 5]
print(sqaures(numbers))

def num_sum(numbers):
    num = []
    for n in numbers:
        num.append(n)
    return sum(num)

print(num_sum(numbers))

def names(*name):
    print(name)
first = 'Ben'
second = 'Eddie', 'Yaw', 'Derrick', 'Ike'
names(second)
