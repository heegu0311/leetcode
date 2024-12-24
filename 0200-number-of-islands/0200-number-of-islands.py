class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # BFS (Level order traversal) 알고리즘
        m = len(grid)
        n = len(grid[0])
        # visited list 배열 자료구조에 grid 형태와 동일한 방문 기록을 True False로 기록
        visited = [[False] * n for _ in range(m)]
        islandCount = 0

        def bfs(graph, start_v):
            (x, y) = start_v
            visited[x][y] = True
            q = deque([start_v])
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            # v 는 vertex의 약자
            # 상하좌우 Vertex 순회 로직
            while q:
                cur_x, cur_y = q.popleft()

                for i in range(4):                    
                    next_v = (cur_x + dx[i], cur_y + dy[i])
                    next_x, next_y = next_v
                    
                    if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                        if graph[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append(next_v)

        # 반복문으로 이중 배열을 순회한다.
        # 방문하지 않았던 섬에 해당하는 "1"을 만나면 bfs 순회를 시작한다.
        for i in range(m):
            for j in range(n):
                start_v = (i, j)
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(grid, start_v)
                    islandCount += 1

        return islandCount
