# LeetCode 20 - Valid Parentheses
# 难度: Easy
# 提交日期: 2026-07-13
# 解法: 栈 + 奇数长度剪枝 + 显式三元表达式判空
# 时间复杂度: O(n) 线性扫描
# 空间复杂度: O(n) 栈的最大深度
#
# 题目:
# 给定一个只包括 '', '', '', '', '', '' 的字符串 s ，判断字符串是否有效。
# 有效需满足：左括号必须用同类型右括号闭合；必须按正确顺序闭合；每个右括号都有对应左括号。
#
# 思路:
# 1. 入口剪枝：检查 len(s) % 2，奇数直接拦截，实现 O(1) 快速失败。
# 2. 建立映射：mapping 存储右括号到左括号的映射，统一收敛判断条件。
# 3. 压栈与出栈：遍历字符串，遇到左括号压入 stack；遇到右括号，利用三元表达式安全弹栈。
# 4. 占位符防御：若弹栈时 stack 已空，赋予 top_element 伪值 '#'，确保随后的等值比对必然失败。
# 5. 残留检查：返回 not stack，确保无多余左括号滞留。
#
# 与#X的区别:
# 与 #3 / #438 等双指针/滑动窗口题目不同：
# 滑动窗口处理的是连续区间的频次与边界移动，而本题属于“嵌套对偶”结构。
# 括号的消除顺序满足“后进先出”（LIFO），必须依赖栈这一特定数据结构暂存历史状态。
#
# 关键语法:
# 1. top_element = stack.pop() if stack else '#' -> 三元表达式。
#    在一行内优雅处理了“右括号溢出导致对空栈执行 pop() 抛出 IndexError”的边界漏洞。
# 2. return not stack -> 隐式布尔值转换，替代 len(stack) == 0，更具 Pythonic 风格。
#
# 学到的:
# 1. 显式控制流的优势：相比于利用 or 运算的短路写法，声明 top_element 变量使逻辑完全显式化，利于面试时的口头表达与排错。
# 2. 伪值防御机制：在异常边界（如空栈）赋予一个绝对不可能匹配成功的特殊符号（如 '#'），可以完美收敛后续的逻辑分支，避免写出复杂的 if-else 嵌套。

class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        mapping = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
