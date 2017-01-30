import re, string

def print_board(dummy_input):
    size = dummy_input.split('x')
    row = int(size[0])
    column = int(size[1])

    print(' --- ' * column)
    for x in range(row):
        print('|   |' * column)
        print(' --- ' * column)

def get_board_values():
    while True:
        usr_input = raw_input("Size of your board (e.g. 3x3): ")
        if re.search( r'^[1-9][0-9]?x[1-9][0-9]?$', usr_input):
            break
        else:
            print('Invalid number. Format has to be "NUMBER"x"NUMBER". Each number cannot be less than 1 or greater than 99')
            continue
    return usr_input

print_board(get_board_values())
