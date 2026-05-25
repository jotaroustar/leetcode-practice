# ============================================================
# LeetCode #199 - Binary Tree Right Side View
# 日期：2026-05-25
# 难度：Medium
# 题目：https://leetcode.com/problems/binary-tree-right-side-view/
# ============================================================
#
# 【思路】BFS层序遍历，取每层最后一个节点
#
# 直接复用#102层序遍历框架
# 唯一区别：result.append(level[-1]) 只取每层最右节点
#
# 时间复杂度：O(n)
# 空间复杂度：O(n)
# ============================================================

from collections import deque

class Solution:
    def rightSideView(self, root):
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level[-1])

        return result
