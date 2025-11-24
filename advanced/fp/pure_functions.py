# The purpose of using paradigms:
# 1. underestandble
# 2. extendable
# 3. maintainable
# 4. memory efficient
# 5. DRY

# In fp we have a separation between data and behavior (in compare to oop)

# Pure function rules:
# 1. Same input sould always be resolved as a same output.
# 2. No side effects (affcting outside world).

# sample
def multiply_by2(list):
    new_list = []

    for item in list:
        new_list.append(item * 2)

    return new_list

print(multiply_by2([1, 2, 3]))


# if we wanted to convert oop to fp:
wizard = {
    'name': 'Merlin',
    'power': 50
}

def attack(char):
    print(f'attack, {char}', char)
