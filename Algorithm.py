# 인접 행렬로 DFS 구현
n = 5
matrix = [[0]*(n+1) for _ in range(n+1)]

matrix[1][2] = 1
matrix[2][1] = 1

matrix[1][3] = 1
matrix[3][1] = 1

matrix[3][4] = 1
matrix[4][3] = 1

matrix[3][5] = 1
matrix[5][3] = 1


visited = [False]*(n+1)
def dfs(matrix, idx, visited):
    stack = [idx]   # 노드를 스택에 넣음
    visited[idx] = True   # 방문한 노드

    while stack:
        current = stack.pop()  # 현재 위치한 노드

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in range(len(matrix[current])-1, -1, -1):
            if matrix[current][child] == 1 and not visited[child]:
                stack.append(child)



