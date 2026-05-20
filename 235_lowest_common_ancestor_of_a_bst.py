# ============================================================
# LeetCode #235 - Lowest Common Ancestor of a Binary Search Tree
# 日期：2026-05-20
# 难度：Medium
# 题目：https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# ============================================================
#
# 【思路】利用BST性质递归
#
# BST核心性质：左子树所有节点 < 根节点 < 右子树所有节点
# 因此数值大小直接对应节点位置：
#
#   p.val和q.val都小于root.val → 答案在左子树
#   p.val和q.val都大于root.val → 答案在右子树
#   一左一右（或其中一个等于root）→ root就是答案
#
# 与普通二叉树不同，BST每次只走一个方向，不需要两边都递归
#
# 时间复杂度：O(h)  h为树高，平衡BST为O(log n)
# 空间复杂度：O(h)  递归栈深度
# ============================================================

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
