# ============================================================
# LeetCode #572 - Subtree of Another Tree
# 日期：2026-05-19
# 难度：Easy
# 题目：https://leetcode.com/problems/subtree-of-another-tree/
# ============================================================
#
# 【思路】双层递归
#
# 外层 isSubtree：遍历 root 的每个节点
# 内层 isSameTree：判断当前节点开始的子树是否与 subRoot 完全相同
#
# 直接复用 #100 isSameTree 逻辑
#
# base case：
#   subRoot is None → True（空树是任何树的子树）
#   root is None   → False（遍历完没找到）
#
# 时间复杂度：O(m*n)  m为root节点数，n为subRoot节点数
# 空间复杂度：O(h)    h为root树高
# ============================================================

class Solution(object):
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
