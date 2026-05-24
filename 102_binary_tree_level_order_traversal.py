# ============================================================
# LeetCode #102 - Binary Tree Level Order Traversal
# 日期：2026-05-24
# 难度：Medium
# 题目：https://leetcode.com/problems/binary-tree-level-order-traversal/
# ============================================================
#
# 【思路】BFS层序遍历
#
# 用队列（deque）逐层处理节点
# 每次while循环开始时队列恰好装着当前层所有节点
# 用len(queue)固定当前层数量，处理完再进入下一层
#
# 与前面DFS题的区别：
#   DFS：递归，纵向深入，用系统栈
#   BFS：队列，横向逐层，用deque
#
# 时间复杂度：O(n)
# 空间复杂度：O(n)  队列最多存一层节点
# ============================================================

from collections import deque

class Solution:
    def levelOrder(self, root):
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

            result.append(level)

        return result
