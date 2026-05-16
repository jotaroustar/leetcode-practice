# LeetCode 021 - Merge Two Sorted Lists
# 难度: Easy
# 提交日期: 2026-05-13
# 解法: 迭代 + 哨兵节点
# 时间复杂度: O(m+n) m,n是两个链表的长度
# 空间复杂度: O(1)
#
# 题目:
# 合并两个升序链表,返回合并后的升序链表头节点
#
# 哨兵节点(dummy node)技巧:
# 创建一个虚假的头节点dummy,curr从dummy开始拼接
# 最后返回dummy.next(跳过哨兵,得到真正的头)
# 好处:不需要单独处理"头节点是谁"的边界问题
#
# 核心逻辑:
# while两个链表都不为None:
#   比较两个链表当前节点的val
#   小的接到curr后面,小的往后走,curr往后走
# 循环结束后把剩余的直接接上(已经有序)
#
# 为什么最后可以直接接剩余部分:
# 剩余部分本身已经有序,且都比已合并部分大
# 直接接上不会破坏有序性
#
# 学到的:
# 1. 哨兵节点:处理头节点不确定时的万能技巧
# 2. 链表拼接:curr.next=节点,curr=curr.next
# 3. 归并思想:两个有序序列合并的通用方法

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 is not None else list2

        return dummy.next
