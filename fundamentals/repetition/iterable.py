# list, dict, tuple, set, string

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False,
}

# keys
for item in user:
    print(item)

for item in user.keys():
    print(item)

# key-value
for item in user.items():
    print(item)

for k, v in user.items():
    print(k, v)

# value
for item in user.values():
    print(item)