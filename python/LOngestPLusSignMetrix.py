class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for (x, y) in mines:
            grid[x][y] = 0

        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        # FIll left and right
        for r in range(n):
            count = 0
            for c in range(n):
                count = count + 1 if grid[r][c] == 1 else 0
                left[r][c] = count
            count = 0
            for c in range(n-1, -1, -1):
                count = count + 1 if grid[r][c] == 1 else 0
                right[r][c] = count

        #fill up and down
        for c in range(n):
            count = 0
            for r in range(n):
                count = count + 1 if grid[r][c] == 1 else 0
                up[r][c] = count
            count = 0
            for r in range(n-1,-1, -1):
                count = count + 1 if grid[r][c] == 1 else 0
                down[r][c] = count
        
        ans = 0
        for r in range(n):
            for c in range(n):
                order = min(left[r][c], right[r][c], up[r][c], down[r][c])
                print(f"order is {order} in location {r, c}")
                ans = max(ans, order)
        return ans



"""
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.


"""