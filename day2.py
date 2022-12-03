scoreboard = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

outcome_2_shape = [
    ['Z', 'X', 'Y'],
    ['X', 'Y', 'Z'],
    ['Y', 'Z', 'X']
]

bonus = {'X': 1, 'Y': 2, 'Z': 3}
offset_A = ord('A')
offset_X = ord('X')


def get_my_score(their_shape, my_shape):
    return scoreboard[ord(their_shape)-offset_A][ord(my_shape)-offset_X] + bonus[my_shape]


def get_my_shape(their_shape, outcome):
    return outcome_2_shape[ord(outcome)-offset_X][ord(their_shape)-offset_A]


f = open("input2.txt", "r")
my_score = 0
for line in f.readlines():
    their_shape, outcome = line.strip().split(' ')
    my_shape = get_my_shape(their_shape, outcome)
    my_score += get_my_score(their_shape, my_shape)

print(my_score)
