class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(r,c):
            searchQueue = deque()
            visit.add((r,c))
            searchQueue.append((r,c))

            while searchQueue:
                row, col = searchQueue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r,c = row+dr, col+dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] =='1' and (r,c) not in visit):
                        searchQueue.append((r,c))
                        visit.add((r,c))


        count = 0 # count islands
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    count += 1
        return count
