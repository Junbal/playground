data = input()
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

move = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]

res = 0
for i in move:
    next_row = row + i[1]
    next_column = column + i[0]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        res += 1

print(res)
