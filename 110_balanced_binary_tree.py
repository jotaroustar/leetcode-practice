# ============================================================
# LeetCode #110 - Balanced Binary Tree
# 日期：2026-05-23
# 难度：Easy
# 题目：https://leetcode.com/problems/balanced-binary-tree/
# ============================================================
#
# 【思路】DFS后序遍历 + -1标记不平衡
#
# dfs返回当前节点高度，发现不平衡时返回-1向上传递
# 避免重复计算，一次遍历解决
#
# 与#543对比：
#   #543：dfs返回深度，self.diameter记录最大直径
#   #110：dfs返回深度，-1表示已不平衡，剪枝提前终止
#
# 时间复杂度：O(n)
# 空间复杂度：O(h)
# ============================================================

class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1
