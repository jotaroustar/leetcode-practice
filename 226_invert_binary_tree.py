# ============================================================
# LeetCode #226 - Invert Binary Tree
# 日期：2026-05-17
# 难度：Easy
# 题目：https://leetcode.com/problems/invert-binary-tree/
# ============================================================
#
# 【思路】递归（DFS前序遍历）
#
# 对每个节点：交换左右子树，再递归处理左右子树
# base case：节点为 None 时直接返回
#
# 与 #104 递归结构完全相同，区别只在于
# 每个节点执行的操作：104取max深度，226交换左右
#
# 时间复杂度：O(n)  每个节点访问一次
# 空间复杂度：O(h)  h为树高，递归栈深度
# ============================================================

class Solution:
    def invertTree(self, root):
        if root is None:
            return root
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
