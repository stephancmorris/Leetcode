# You are given a binary matrix Grid where 0s represent land and 1s represent rocks that can not be traversed.

# Return the number of unique paths from the top-left corner of Grid to the bottom-right corner such that all traversed cells are land cells. You may only move vertically or horizontally through land cells. For an individual unique path you cannot visit the same cell twice.


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # Determine the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])

        # Helper function for DFS
        def helper(grid: List[List[int]], r: int, c: int, visit: set) -> int:
            # Base case: return 0 if out of bounds, cell is blocked, or already visited
            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 1):
                return 0
            
            # Base case: return 1 if the bottom-right cell is reached
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            # Mark the current cell as visited
            visit.add((r, c))

            # Initialize count of paths
            count = 0
            # Recursive DFS calls for adjacent cells (down, up, right, left)
            count += helper(grid, r + 1, c, visit)
            count += helper(grid, r - 1, c, visit)
            count += helper(grid, r, c + 1, visit)
            count += helper(grid, r, c - 1, visit)

            # Backtrack: remove the current cell from visited before returning
            visit.remove((r, c))
            return count

        # Start DFS from the top-left cell (0, 0)
        return helper(grid, 0, 0, set())

# **Time Complexity:**
# - The time complexity of this algorithm is a bit tricky to determine precisely because it depends on the structure of the grid.
# - In the worst case, if the grid allows for many paths, the algorithm explores all possible paths. This can be exponential in the size of the grid, potentially O(4^(ROWS*COLS)) because at each cell, there are 4 possible directions to explore.
# - However, in many practical cases, especially when the grid contains many blocked cells (1s), the number of paths to explore will be significantly less.

# **Space Complexity:**
# - The space complexity is primarily due to the recursion stack and the `visit` set.
# - The recursion stack's maximum depth can go up to the total number of cells in the grid in the worst case, making the space complexity O(ROWS*COLS).
# - The `visit` set can also hold at most ROWS*COLS elements if all cells are visited.

# This DFS approach is a common method for exploring paths in a grid, with backtracking to ensure all possibilities are considered. The complexity can vary greatly based on the grid's structure.