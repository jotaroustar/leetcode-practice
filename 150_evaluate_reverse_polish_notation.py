# LeetCode 150 - Evaluate Reverse Polish Notation
# 难度: Medium
# 提交日期: 2026-07-16
# 解法: 单栈模拟运算 + 负数除法向零截断处理
# 时间复杂度: O(n) tokens 数组仅需单次单向扫描
# 空间复杂度: O(n) 最坏情况下栈中存储全部操作数
#
# 题目:
# 给你一个字符串数组 tokens ，表示一个根据逆波兰表示法表示的算术表达式。
# 有效的算符包括 '+'、'-'、'*' 和 '/' 。每个操作数可以是整数，也可以是另一个表达式。
# 两个整数之间的除法总是向零截断。
#
# 思路:
# 1. 建立单栈 stack 暂存数字。
# 2. 遍历 tokens 数组，使用 hash set 存储四则运算符，方便 O(1) 判定。
# 3. 遇到数字直接转 int 压栈。
# 4. 遇到算符，依次弹出 num2 (右操作数) 和 num1 (左操作数)，进行相应运算后将结果压回栈。
# 5. 针对 Python 特有的向零截断除法，使用 int(num1 / num2) 替代 floor division (//)。
#
# 与#X的区别:
# 与 #20 (有效的括号) 相比：
# #20 是遇到“右括号”立刻与栈顶“左括号”抵消（字符对齐消除）。
# #150 是遇到“运算符”时弹出两个“操作数”合并计算，属于“数据聚合消除”，本质上是 AST（抽象语法树）的栈式求值。
#
# 关键语法:
# 1. int(num1 / num2) -> 解决 Python 中 `//` 无法向零截断负数除法的物理限制。
#
# 学到的:
# 1. 操作数方向性：在双元操作（如减、除）中，先出栈的是右操作数，后出栈的是左操作数，顺序敏感，绝不能写反。
# 2. 语言底层陷阱：Floor division (//) 与 Truncation division (int(/)) 在处理负数时的差异是经典的平台相关性陷阱，在跨语言（如从 Python 转换到 C++/Go）移植代码时必须保持敏感。

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(int(float(num1) / num2))
            else:
                stack.append(int(token))
                
        return stack[0]
