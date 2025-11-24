class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing!')

# subclass or derived class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: left- {self.num_arrows}')

wizard = Wizard('Merlin', 50)
archer = Archer('Robin', 30)

# the polymorphism
def player_attack(char):
    char.attack()

player_attack(wizard)
player_attack(archer)