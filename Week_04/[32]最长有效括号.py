# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 891 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0  # 最大合法长度(返回值)
        stack = [-1, ]  # stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
        for i, ch in enumerate(s):
            if '(' == ch:  # 左括号
                stack.append(i)
            elif len(stack) > 1:  # 右括号，且有成对左括号
                stack.pop()  # 成对匹配
                ans = max(ans, i - stack[-1])
            else:  # 非法的右括号
                stack[0] = i
        return ans


# leetcode submit region end(Prohibit modification and deletion)
