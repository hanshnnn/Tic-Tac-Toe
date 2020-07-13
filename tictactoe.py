def print_field():
    print('---------')
    print(f'| {ox[0]} {ox[1]} {ox[2]} |')
    print(f'| {ox[3]} {ox[4]} {ox[5]} |')
    print(f'| {ox[6]} {ox[7]} {ox[8]} |')
    print('---------')


def split(word):
    x = []
    for a in word:
        if a != ' ':
            x.append(a)
    return x


def check_if_empty(y):
    global statement
    global player
    global ox1, ox2, ox3
    global matrix_ox
    if ox[y] != ' ':
        print('This cell is occupied! Choose another one!')
        statement = 'no'
    else:
        ox[y] = player
        statement = 'yes'
        ox1 = [ox[0], ox[1], ox[2]]  # updates new table
        ox2 = [ox[3], ox[4], ox[5]]
        ox3 = [ox[6], ox[7], ox[8]]
        matrix_ox = [ox1, ox2, ox3]
        print_field()


def input_check(x):
    checker = split(x)
    global statement
    statement = 'yes'
    for a in checker:  # checks non-numerical/incorrect input
        if 48 < ord(a) < 57:
            if ord(a) != 49 and ord(a) != 50 and ord(a) != 51:
                print('Coordinates should be from 1 to 3!')
                statement = 'no'
        else:
            print('You should enter numbers!')
            statement = 'no'
            break
    if statement == 'yes':
        if x == '1 1':
            check_if_empty(6)
        elif x == '2 1':
            check_if_empty(7)
        elif x == '3 1':
            check_if_empty(8)
        elif x == '1 2':
            check_if_empty(3)
        elif x == '2 2':
            check_if_empty(4)
        elif x == '3 2':
            check_if_empty(5)
        elif x == '1 3':
            check_if_empty(0)
        elif x == '2 3':
            check_if_empty(1)
        elif x == '3 3':
            check_if_empty(2)


def column(x):  # extract column
    global matrix_ox
    return [row[x] for row in matrix_ox]


def check_if_win():
    global matrix_ox, winner
    for i in range(3):
        if matrix_ox[i] == ['O', 'O', 'O'] or column(i) == ['O', 'O', 'O']:
            winner = 'O wins'
        if matrix_ox[i] == ['X', 'X', 'X'] or column(i) == ['X', 'X', 'X']:
            winner = 'X wins'
    if ox[0] == 'O' and ox[4] == 'O' and ox[8] == 'O':
        winner = 'O wins'
    elif ox[2] == 'O' and ox[4] == 'O' and ox[6] == 'O':
        winner = 'O wins'
    elif ox[0] == 'X' and ox[4] == 'X' and ox[8] == 'X':
        winner = 'X wins'
    elif ox[2] == 'X' and ox[4] == 'X' and ox[6] == 'X':
        winner = 'X wins'
    elif ox.count('X') + ox.count('O') == 9:
        winner = 'Draw'


winner = ''
player = 'X'
ox = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print_field()
statement = ''
ox1 = [ox[0], ox[1], ox[2]]
ox2 = [ox[3], ox[4], ox[5]]
ox3 = [ox[6], ox[7], ox[8]]
matrix_ox = [ox1, ox2, ox3]
while not any(winner):
    coordinate = input('Enter the coordinates: > ')
    input_check(coordinate)
    while statement == 'no':
        coordinate = input('Enter the coordinates: > ')
        input_check(coordinate)
    if statement == 'yes':
        if player == 'X':  # switch player
            player = 'O'
        else:
            player = 'X'
    check_if_win()
print(winner)


'''

counter_X = 0
counter_O = 0



for i in range(3):
    for j in range(3):
        if matrix_ox[i] == ['X', 'X', 'X'] or column(i) == ['X', 'X', 'X']:
            if matrix_ox[j] == ['O', 'O', 'O'] or column(j) == ['O', 'O', 'O']:
                winner = 'Impossible'
                break
        if matrix_ox[i][j] == 'X':  # counts the number of X and O
            counter_X += 1
        elif matrix_ox[i][j] == 'O':
            counter_O += 1


if winner == '':

    elif abs(counter_X - counter_O) > 1:
        winner = 'Impossible'
    else:
        winner = 'Game not finished'
print(winner)
'''