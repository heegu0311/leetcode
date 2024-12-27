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
 