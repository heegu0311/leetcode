from collections import deque

# BFS
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        q = deque()
        visited = len(rooms) * [False]
        q.append(rooms[0])
        visited[0] = True

        while q:
            keys = q.popleft()

            for key in keys:
                if visited[key] == False:
                    q.append(rooms[key])

                visited[key] = True
        
        return all(visited)
 
# s1 = Solution()
# print(s1.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))


# DFS
class Solution2:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = len(rooms) * [False]

        def dfs(key: int):
            visited[key] = True
            for next_key in rooms[key]:
                if not visited[next_key]:
                    dfs(next_key)

        dfs(0)
        
        return all(visited)