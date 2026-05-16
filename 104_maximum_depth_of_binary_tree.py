# ============================================================
# LeetCode #104 - Maximum Depth of Binary Tree
# 日期：2026-05-16
# 难度：Easy
# 题目：https://leetcode.com/problems/maximum-depth-of-binary-tree/
# ============================================================
#
# 【思路】递归（DFS后序遍历）
#
# 核心公式：当前节点深度 = max(左子树深度, 右子树深度) + 1
# base case：节点为 None 时返回 0
# 从叶子节点向上逐层返回，根节点汇总最终结果
#
# 时间复杂度：O(n)  每个节点访问一次
# 空间复杂度：O(h)  h为树高，递归栈深度
# ============================================================

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        lft = 1 + self.maxDepth(root.left)
        rgt = 1 + self.maxDepth(root.right)
        
        return max(lft, rgt)
