class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self): # changed the default dunder of the class 
        return f'{self.color}'

    def __del__(self):
        print('deleted!')

    def __call__(self):
        return('yes???!!!')

action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))
print(action_figure()) # calling the class!
del action_figure # like JS most of the time it's better to don't use del keyword! It actually delete the instance really!


# EX1
class SuperList(list):
    def __len__(self):
        return 1000

super_list = SuperList()

print(len(super_list))
super_list.append(5)
print(super_list[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))