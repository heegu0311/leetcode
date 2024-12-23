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


            # v 는 vertex의 약자
            # 상하좌우 Vertex 순회 로직
            while q:
                cur_v = q.popleft()

                right_v = (cur_v[0], cur_v[1] + 1)
                (right_x, right_y) = right_v

                if right_y < len(graph[0]) and graph[right_x][right_y] != "0" and not visited[right_x][right_y]:
                    visited[right_x][right_y] = True
                    q.append(right_v)

                left_v = (cur_v[0], cur_v[1] - 1)
                (left_x, left_y) = left_v

                if left_y > -1 and graph[left_x][left_y] != "0" and not visited[left_x][left_y]:
                    visited[left_x][left_y] = True
                    q.append(left_v)

                up_v = (cur_v[0] - 1, cur_v[1])
                (up_x, up_y) = up_v

                if up_x > -1 and graph[up_x][up_y] != "0" and not visited[up_x][up_y]:
                    visited[up_x][up_y] = True
                    q.append(up_v)

                bottom_v = (cur_v[0] + 1, cur_v[1])
                (bottom_x, bottom_y) = bottom_v

                if bottom_x < len(graph) and graph[bottom_x][bottom_y] != "0" and not visited[bottom_x][bottom_y]:
                    visited[bottom_x][bottom_y] = True
                    q.append(bottom_v)

        # 반복문으로 이중 배열을 순회한다.
        # 방문하지 않았던 섬에 해당하는 "1"을 만나면 bfs 순회를 시작한다.
        for i in range(m):
            for j in range(n):
                start_v = (i, j)
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(grid, start_v)
                    islandCount += 1

        return islandCount
