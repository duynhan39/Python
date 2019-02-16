import sys

def solve(board):
    m, n = len(board), len(board[0])
    '''create adjacency list
    rows[0] has all the nodes in 1st row
    rows[1] has all the nodes in 2nd row
    etc.
    cols[0] has all the nodes in 1st column
    cols[1] has all the nodes in 2nd column
    etc.'''
    rows, cols = [set() for i in range(m)], [set() for j in range(n)]
    for i in range(m):
        for j in range(n):
            if board[i][j] is 'O':
                rows[i].add(j)
                cols[j].add(i)

    #count the degree (number of neighbors) of every orb
    degrees = dict()
    for i in range(m):
        for j in rows[i]:
            degree = len(rows[i]) + len(cols[j]) - 2
            if degree > 0:
                degrees[(i, j)] = degrees

    #erase the node with minimum positive degree until all nodes have 0 degree
    while degrees:
        erase_orb(degrees, board, rows, cols)

    #output
    for row in board:
        print row


#erase the orb with the minimum degree
def erase_orb(degrees, board, rows, cols):
    #find the node with minimum positive degree
    i, j = min(degrees.items(), key=lambda x: x[1])[0]
    #erase this node
    rows[i].remove(j)
    cols[j].remove(i)
    degrees.pop((i, j))
    board[i][j] = 'X'
    print 'erase ', (i, j)

    #remove one degree from every neighbor of the node erased
    for y in rows[i]:
        degrees[(i, y)] -= 1
        if degrees[(i, y)] is 0:
            degrees.pop((i, y))

    for x in cols[j]:
        degrees[(x, j)] -= 1
        if degrees[(x, j)] is 0:
            degrees.pop((x, j))


mat = sys.stdin.readlines()
#mat = [ x[:-1] for x in mat ]
m = [ [y for y in x[:-1]] for x in mat ]

print m

#solve(mat)


solve([
    ['X', 'X', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'X', 'X', 'X', 'X'],
    ['O', 'X', 'X', 'X', 'X', 'O'],
    ['X', 'X', 'O', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X', 'X', 'O']
    ])
