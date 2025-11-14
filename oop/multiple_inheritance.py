class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'attacking with arrows: left- {self.arrows}')

    def run(self):
        print('ran really fast')

# this class will inherit from Wizard first and then Archer!
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb = HybridBorg('Borgy', 50, 100)
hb.run()
hb.attack()
hb.sign_in()