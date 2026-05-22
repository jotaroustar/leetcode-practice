# =========================================================
# LeetCode #543 - Diameter of Binary Tree
# 日期: 2026-05-22
# 难度: Easy
# 题目: https://leetcode.com/problems/diameter-of-binary-tree/
# =========================================================
#
# 【思路】DFS + 后序遍历
#
# 核心：
# 一个节点的直径 =
# 左子树最大深度 + 右子树最大深度
#
# DFS 返回当前节点最大深度：
# max(left, right) + 1
#
# 遍历过程中不断更新最大直径
#
# 时间复杂度: O(n)
# 空间复杂度: O(h)
# =========================================================


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        dfs(root)

        return self.diameter
