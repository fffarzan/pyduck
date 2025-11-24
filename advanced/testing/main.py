def do_stuff(num=0):
    if num == None:
        return 'Please enter a number'

    try:
        return int(num) + 5
    except ValueError as err:
        return err