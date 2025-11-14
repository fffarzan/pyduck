class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email) # to inherit the vars inside of parent class
        super().__init__(email) # to inherit the vars inside of parent class
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

wizard = Wizard('Merlin', 50, 'merlin@gmail.com')
print(wizard.email)