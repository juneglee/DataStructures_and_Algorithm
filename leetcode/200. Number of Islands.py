'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
# 1을 육지로 0을 물로 가정한 2D 그리드 맵이 주어졌을 때 섬의 개수를 게산하라
# (연결되어 있는 1의 덩어리 개수를 구하라 )
# 입력값이 정확히 그래프는 아니지만 사실상 동서남북이 모두 연결된 그래프로 가정하고 동일한 형태로 처리할 수 있으며,
# 네 방향 각가 DPS 재귀를 이용해 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수를 파악할 수 잇다
def numIslands(self, grid):
    def dfs(i, j):
        # 땅이 경우, 더이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != "1":
            return

            grid[i][j] = 0
            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count +=1
        return count

# Runtime: 280 ms, faster than 79.46% of Python online submissions for Number of Islands.
# Memory Usage: 28.9 MB, less than 50.05% of Python online submissions for Number of Islands.