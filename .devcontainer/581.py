G = [[2, 4, 5, 4, 2], [4, 9, 12, 9, 4], [5, 12, 15, 12, 5], [4, 9, 12, 9, 4],[ 2, 4, 5, 4, 2]]
for row in G:
    for i in range (len(row)):
        row[i] = row[i] / 2
nr, nc = G.shape

print(nr, nc)