# 인접 리스트로 DFS 구현
n = 5
graph = [[] for _ in range(n+1)]

graph[1] = [2, 3]
graph[2] = []
graph[3] = [4, 5]
graph[4] = []
graph[5] = []

visited = [False]*(n+1)
def dfs(graph, idx, visited):
    stack = [idx]   # 노드를 스택에 넣음
    visited[idx] = True   # 방문한 노드

    while stack:    # 스택이 빌 때까지 반복
        current = stack.pop()  # 현재 위치한 노드

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in graph[current]:
            if not visited[child]:
                stack.append(child)

dfs(graph, 1, visited)




