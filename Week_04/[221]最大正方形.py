# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。 
# 
#  示例: 
# 
#  输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4 
#  Related Topics 动态规划 
#  👍 505 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getWidth(self,num):
        w = 0
        while num > 0:
            num &= num << 1
            w += 1
        return w


    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums = [int(''.join(n), base=2) for n in matrix]
        res, n = 0, len(nums)
        for i in range(n):
            temp = nums[i]
            for j in range(i, n):
                temp &= nums[j]
                w = self.getWidth(temp)
                h = j - i + 1
                res = max(res, min(w, h))
        return res * res


# leetcode submit region end(Prohibit modification and deletion)
