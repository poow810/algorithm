from collections import deque
n = 5
matrix = [[0]*(n+1) for _ in range(n+1)]

matrix[1][2] = 1
matrix[2][1] = 1

matrix[1][3] = 1
matrix[3][1] = 1

matrix[2][5] = 1
matrix[5][2] = 1

matrix[3][4] = 1
matrix[4][3] = 1

visited = [False]*(n+1)

def bfs(matrix, idx, visited):
    queue = deque()
    queue.append(idx)

    while queue:
        current = queue.popleft()

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in range(len(matrix[current])):
            if matrix[current][child] == 1 and not visited[child]:
                queue.append(child)

bfs(matrix, 1, visited)

