class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        # BFS (Level order traversal) 알고리즘
        m = len(grid)
        n = len(grid[0])
        # visited list 배열 자료구조에 grid 형태와 동일한 방문 기록을 True False로 기록
        visited = [[False] * n for _ in range(m)]
        shortestPath = -1

        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
           return -1


        (x, y, move) = (0, 0, 1)
        visited[x][y] = True
        q = deque([(x, y, move)])
        # 12시 방향에서 시작해서 시계 방향으로 다음 Vertex 확인하는 dx, dy

        dx = [-1, 1, -1, 1, -1, 0, 1, 0]
        dy = [1, 1, -1, -1, 0, 1, 0, -1]

        # v 는 vertex의 약자
        # 상하좌우 Vertex 순회 로직
        while q:
            cur_x, cur_y, cur_move = q.popleft()

            if cur_x == m-1 and  cur_y == n-1:
                shortestPath = cur_move
                break

            for i in range(8):                    
                next_v = (cur_x + dx[i], cur_y + dy[i])
                next_x, next_y = next_v
                
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y, cur_move + 1))

        return shortestPath