# Hiding information and giving access to what is neccessary.

class PlayerChar:
    def __init__(self, name, age): # double underscore is also a convention that you shouldn't touch that method.
        self._name = name  # convention for private vars
        self._age = age

    def run(self):
        print(f'run, {self._name}')

player1 = PlayerChar('Jeff', 42)
print(player1.run())