# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。 
# 
#  示例 1: 
# 
#  
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#  
# 
#  示例 2: 
# 
#  
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#  
# 
#  注意: 
# 
#  
#  输入的字符串长度不会超过1000。 
#  
#  Related Topics 字符串 动态规划 
#  👍 295 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        L = len(s)
        cnt = 0
        # 以某一个元素为中心的奇数长度的回文串的情况
        for center in range(L):
            left = right = center
            while left >= 0 and right < L and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        # 以某对元素为中心的偶数长度的回文串的情况
        for left in range(L - 1):
            right = left + 1
            while left >= 0 and right < L and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1

        return cnt

# leetcode submit region end(Prohibit modification and deletion)
