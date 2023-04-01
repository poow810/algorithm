from collections import deque
n = 5
graph = [[] for _ in range(n+1)]
graph[1] = [2, 3]
graph[2] = [5]
graph[3] = [4]
graph[4] = []
graph[5] = []

visited = [False]*(n+1)

def bfs(graph, idx, visited):
    queue = deque()
    queue.append(idx)

    while queue:
        current = queue.popleft()

        if not visited[current]:
            print(current)
            visited[current] = True


        for child in graph[current]:
            queue.append(child)


bfs(graph, 1, visited)

