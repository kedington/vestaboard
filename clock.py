from datetime import datetime
from vestaboard import board_height, board_width
from test_api import update_text

# Get the current time and the 4 digits to display
now = datetime.now()
hour = now.hour
minute = now.minute
digits = [hour // 10, hour % 10, minute // 10, minute % 10]

colon = set([(10,1), (11,1), (10,2), (11,2), (10,4), (11,4), (10,5), (11,5)])

# http://jsfiddle.net/xdg3k1ra
numbers = {0: set([(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5),(2,5),(1,5),(0,5),(0,4),(0,3),(0,2)]),
           1: set([(2,1),(2,2),(2,3),(2,4),(2,5)]),
           2: set([(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(2,3),(1,3),(0,3),(0,4),(0,5),(1,5),(2,5),(3,5)]),
           3: set([(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(2,3),(1,3),(0,3),(3,4),(3,5),(2,5),(1,5),(0,5)]),
           4: set([(0,1),(0,2),(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,4),(3,5)]),
           5: set([(3,1),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3),(3,3),(3,4),(3,5),(2,5),(1,5),(0,5)]),
           6: set([(3,1),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3),(3,3),(3,4),(3,5),(2,5),(1,5),(0,5),(0,4)]),
           7: set([(0,1),(1,1),(2,1),(3,1),(3,2),(3,3),(3,4),(3,5)]),
           8: set([(0,1),(1,1),(3,1),(2,1),(0,2),(0,3),(1,3),(2,3),(3,3),(3,2),(3,4),(3,5),(2,5),(1,5),(0,5),(0,4)]),
           9: set([(0,1),(0,2),(1,1),(2,1),(3,1),(3,2),(3,3),(0,3),(1,3),(2,3),(3,4),(3,5)])}

# offsets to shift the numbers over
offsets = [0, 5, 13, 18]

points = set()
for num in range(4):
        points = points.union(map(lambda x: (x[0] + offsets[num], x[1]), numbers[digits[num]]))
points = points.union(colon)


board = []

for y in range(board_height):
        inner = []
        for x in range(board_width):
                if (x,y) in points:
                        inner.append('{69}')
                else:
                        inner.append('{62}')
        board.append(inner)

text = ''
for row in board:
        text += ''.join(row)

update_text(text)
