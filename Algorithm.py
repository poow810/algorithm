from collections import deque


def bfs(matrix, idx, visited):
    queue = deque()
    queue.append(idx)

    while queue:
        current = queue.popleft()

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in range(len(matrix[current])):
            if matrix[current][child] == 1 and visited[child]:
                queue.append(child)

bfs(matrix, 1, visited)

