# ============================================================
# LeetCode #100 - Same Tree
# 日期：2026-05-18
# 难度：Easy
# 题目：https://leetcode.com/problems/same-tree/
# ============================================================
#
# 【思路】递归
#
# 对每个节点判断三个条件：
#   1. 当前节点值相同 p.val == q.val
#   2. 左子树相同
#   3. 右子树相同
#
# base case：
#   两个都是 None → True
#   一个 None 一个不是 → False
#
# 与 #104 #226 递归结构完全相同
#
# 时间复杂度：O(n)  每个节点访问一次
# 空间复杂度：O(h)  h为树高，递归栈深度
# ============================================================

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
