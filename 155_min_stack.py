# LeetCode 155 - Min Stack
# 难度: Medium
# 提交日期: 2026-07-15
# 解法: 双栈同步更新机制（数据栈 + 同步辅助最小栈）
# 时间复杂度: push, pop, top, getMin 均为 O(1)
# 空间复杂度: O(n) 辅助栈在最坏情况下需要存储与数据栈等量的数据
#
# 题目:
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 实现 MinStack 类:
# - MinStack() 初始化堆栈对象。
# - void push(int val) 将元素 val 推入堆栈。
# - void pop() 删除堆栈顶部的元素。
# - int top() 获取堆栈顶部的元素。
# - int getMin() 获取堆栈中的最小元素。
#
# 思路:
# 1. 双栈物理同步：设计 data_stack 存储数据，min_stack 存储对应步骤的历史最小值。
# 2. 压栈决策：
#    - 数据栈直接 append(val)。
#    - 辅助栈对比 val 与当前 min_stack[-1]。若 val 更小，压入 val；否则重复压入 min_stack[-1]。
#    - 这一步确保了两栈长度永远一致，且 min_stack 的栈顶永远是 data_stack 对应的实时最小值。
# 3. 弹栈决策：
#    - data_stack 与 min_stack 同时执行 pop()，无需进行复杂的逻辑比对，天然保持状态同步。
# 4. 读栈顶与读最小值：
#    - top() 返回 data_stack[-1]。
#    - getMin() 返回 min_stack[-1]。
#
# 与#X的区别:
# 与 #232 (用栈实现队列) 相比：
# #232 引入双栈是为了“颠倒数据流向”（LIFO -> FIFO），通过单向倾倒实现顺序翻转。
# #155 引入双栈是为了“暂存历史状态”（状态备份），两个栈数据流向完全平行，用于解决 pop 后状态丢失的痛点。
#
# 关键语法:
# 1. min_val = self.min_stack[-1] if self.min_stack else val
#    - 初始化压栈时，若辅助栈为空，当前 val 即为历史最小值。
# 2. self.min_stack.append(min(val, min_val))
#    - 利用 Python 内置的 min() 函数进行轻量数值比对。
#
# 学到的:
# 1. 状态降维与备份：面对“因元素移除导致全局状态（如极值）失效”的问题，最稳妥的方案是为每个状态节点配备一个“状态快照（Snapshot）”，即辅助数据结构。
# 2. 物理同步消灭逻辑分支：保持 data_stack 和 min_stack 长度与操作的 1:1 同步，虽然多耗费了微量空间，但消灭了 pop 时的条件分支判定，使代码健壮性极高。

class MinStack(object):

    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, val):
        self.data_stack.append(val)
        if self.min_stack:
            current_min = min(val, self.min_stack[-1])
        else:
            current_min = val
        self.min_stack.append(current_min)

    def pop(self):
        if self.data_stack:
            self.data_stack.pop()
            self.min_stack.pop()

    def top(self):
        return self.data_stack[-1] if self.data_stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
