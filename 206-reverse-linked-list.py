# LeetCode 206 - Reverse Linked List
# 难度: Easy
# 提交日期: 2026-05-12
# 解法: 迭代(三指针)
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 题目:
# 反转一个链表,返回新的头节点
#
# 链表节点结构:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# 三指针思路:
# prev: 指向已反转部分的最后一个节点(初始None)
# curr: 指向当前处理的节点
# next_node: 临时保存curr.next防止断链
#
# 每步操作:
# 1. 保存next_node = curr.next (先保存,防断链)
# 2. curr.next = prev           (反转指向)
# 3. prev = curr                (prev右移)
# 4. curr = next_node           (curr右移)
#
# 为什么返回prev不返回curr:
# 循环结束时curr=None(越过末尾)
# prev停在最后一个节点=反转后的新头节点
#
# 为什么先保存next_node:
# curr.next=prev会覆盖原来的next
# 必须提前保存否则找不到下一个节点
#
# 学到的:
# 1. 链表节点:val存值,next指向下一个
# 2. 操作链表时必须先保存next防止断链
# 3. while curr is not None 遍历链表的标准写法
# 4. 反转链表是链表题的基础,后续题目都会用到

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next   # 先保存下一个
            curr.next = prev        # 反转指向
            prev = curr             # prev右移
            curr = next_node        # curr右移

        return prev
