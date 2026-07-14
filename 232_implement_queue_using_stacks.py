# LeetCode 232 - Implement Queue using Stacks
# 难度: Easy
# 提交日期: 2026-07-14
# 解法: 双栈单向倾倒机制（输入栈 + 输出栈）
# 时间复杂度: push 为 O(1)，pop/peek 均摊(Amortized) 为 O(1)
# 空间复杂度: O(n) 两个栈合起来共存储 n 个队列元素
#
# 题目:
# 请仅使用两个栈实现先入先出（FIFO）队列。
# 实现的队列应支持普通队列的所有功能（push、pop、peek、empty）。
# 只能使用标准的栈操作：即 append()、pop()、[-1]（查看顶部）以及 len()。
#
# 思路:
# 1. 双栈配置：定义 in_stack 专门接纳新数据，out_stack 专门负责吐出数据。
# 2. 负负得正：数据从 in_stack 倒入 out_stack 时，底层的物理顺序会彻底反转，刚好从 LIFO 变成 FIFO。
# 3. 惰性倾倒（加分项）：不要每次 push 都倒水！只有当出队(pop/peek)时，如果 out_stack 空了，才把 in_stack 的全部数据一次性倒过来。
# 4. 高级复用：pop() 的本质就是“先 peek() 确保输出栈有数，然后执行真正的弹栈”。
#
# 与#X的区别:
# 与 #20 (有效的括号) 相比：
# #20 是使用单栈来做局部状态的“即时消除”（匹配成功立刻弹栈）。
# #232 是使用双栈通过“空间转移”来强行改变数据流的进出顺序，属于结构设计类题目。
#
# 关键语法:
# 1. self.out_stack.pop() -> 严格遵守题目限制，只从列表末尾弹栈（等同于栈顶 pop）。
# 2. self.out_stack[-1] -> Python 中获取栈顶元素的标准 O(1) 语法。
#
# 学到的:
# 1. 均摊复杂度（Amortized Complexity）的辩证思维：单次“倒水”虽是 O(n)，但每个元素一生只进出两个栈各一次，均摊下来依然是 O(1)。
# 2. DRY 原则（Don't Repeat Yourself）：通过让 pop() 直接调用 peek()，省去了在两个函数里重复写 while 循环倒水的高额代码冗余。

class MyQueue(object):

    def __init__(self):
        self.in_stack = []   
        self.out_stack = []  

    def push(self, x):
        self.in_stack.append(x)
        
    def pop(self):
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                        
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack
