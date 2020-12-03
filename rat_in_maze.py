'''
backtracking + dp
backtracking because if we dont get a solution, we backtrack by popping elements
from the path variable
and dp because we maintain a seen matrix called visited to not do iterations again

'''

def solution(mat):

    path = []
    visited = []
    rows = len(mat)
    cols = len(mat[0])
    sindex = [0,0]
    eindex =[rows-1,cols-1]

    i,j = 0,0
    cur = [0,0]

    path.append(cur)
    visited.append(cur)

    while(i <= eindex[0] and j <= eindex[1]):

        # check if the pos below the current pos is a valid place to move
        if cur[0] + 1 <= eindex[0] and mat[cur[0] + 1][cur[1]] == 1 and [cur[0] + 1,cur[1]] not in visited:
            i = cur[0]
            i = i + 1

            cur = [i,cur[1]]
            path.append(cur)
            visited.append(cur)

            if cur[0] == eindex[0] and cur[1] == eindex[1]:
                return path

            continue

        # check if the pos on the right of the current pos is a valid place to move
        if cur[1] + 1 <= eindex[1] and mat[cur[0]][cur[1]+1] == 1 and [cur[0],cur[1]+1] not in visited:
            j = cur[1]
            j = j + 1
            cur = [cur[0],j]
            path.append(cur)
            visited.append(cur)

            if cur[0] == eindex[0] and cur[1] == eindex[1]:
                return path

            continue

        # if there is no way to move ahead from the current node, remove that node
        # from path and find an alternate way from the previous node

        else:
            path.pop()

            # as when we dont have any solution, we wont have any way to move
            # forward so we will keep popping possible pos from the path list
            # and there will be a point we will eliminate all elements
            if len(path) == 0:
                return "No way"

            cur = path[0]

            if cur[0] == eindex[0] and cur[1] == eindex[1]:
                return path

            continue

    return "No way"

matrix = [
            [ 1, 1, 1, 1, 0 ],
            [ 1, 0, 1, 0, 1 ],
            [ 0, 1, 1, 0, 1 ],
            [ 1, 1, 1, 1, 1 ]
         ]

ans = solution(matrix)
print(ans)
