class User:
    def sign_in(self):
        print('logged in')

# subclass or derived class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: left- {self.num_arrows}')

wizard = Wizard('Merlin', 50)
archer = Archer('Robin', 100)
print(wizard.sign_in())
wizard.attack()
archer.attack()

print(isinstance(wizard, Wizard))
print(isinstance(wizard, User))

# everything in python is based on an `object`. all the built-in dunders from the object base class.
print(isinstance(wizard, object))