class NameOfClass:
    class_attr = 'value'

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        # code
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        # code
        pass

    @staticmethod
    def stc_method(param1, param2):
        # code
        pass

class PlayerChar:
    membership = True # class attrs

    def __init__(self, name, age):
        if (self.membership): # or PlayerChar.membership because membership is a class attr.
            self.name = name # attrs
            self.age = age

    def run(self):
        print(f'run, {self.name}') # We can't use PlayerChar.name here because name isn't a class attr.
        return 'done'

    @classmethod # decorator
    def adding_things(cls, num1, num2): # cls is the class.
        print(cls('Ted', num1 + num2))
        return num1 + num2 

    @staticmethod # difference with classmethod: you haven't access to cls
    def adding_things2(num1, num2): # cls is the class.
        return num1 + num2

player1 = PlayerChar('Jeff', 42)
player2 = PlayerChar('Brad', 24)

print(player1.run())
print(player1, player2) # different instances store different places in memory
print(PlayerChar.adding_things(2, 3))
print(PlayerChar.adding_things(3, 4))