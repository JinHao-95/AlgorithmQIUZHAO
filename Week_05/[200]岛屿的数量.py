# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 707 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i: int, j: int) -> None:
            if i == 0 or j == 0 or i == x - 1 or j == y - 1 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        x = len(grid) + 2
        y = len(grid[0]) + 2
        grid = [["0"] * x] + [["0"] + i + ["0"] for i in grid] + [["0"] * x]
        ret = 0
        for i in range(1, x - 1):
            for j in range(1, y - 1):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ret += 1
        return ret

# leetcode submit region end(Prohibit modification and deletion)
