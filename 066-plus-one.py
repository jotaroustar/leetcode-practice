# LeetCode 066 - Plus One
# 难度: Easy
# 提交日期: 2026-05-?? (填实际日期)
# 解法: Python "字符串-整数转换" 取巧解法
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 题目:
# 给定数组表示的非负整数,各位数字按高位到低位存储
# 给整数加1,返回结果数组
#
# 思路(取巧解法):
# 1. map(str, digits) - 每个数字转字符串
# 2. "".join() - 拼接成字符串"123"
# 3. int() + 1 - 转整数加1
# 4. 列表推导式 [int(d) for d in str(num)] - 拆回数组
#
# 优点: 代码极简,3行搞定,自动处理进位
# 缺点: 依赖Python的大整数支持,在C/C++/Java会溢出
#
# 学到的Python语法:
# 1. map(函数, 可迭代对象) - 对每个元素应用函数
# 2. "分隔符".join(列表) - 字符串列表连接
# 3. 列表推导式 [表达式 for 变量 in 可迭代对象]
#
# 另一种解法: 模拟加法(更通用,面试推荐)
# def plusOne(self, digits):
#     n = len(digits)
#     for i in range(n - 1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits
#         digits[i] = 0
#     return [1] + digits

class Solution(object):
    def plusOne(self, digits):
        num_str = "".join(map(str, digits))
        num = int(num_str) + 1
        return [int(d) for d in str(num)]
