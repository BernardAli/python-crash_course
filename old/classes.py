class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


defender = Dog('defender', 2.5)
print(defender.age)
print(defender.name)
defender.sit()
defender.roll_over()