# ============================================================
# LeetCode #101 - Symmetric Tree
# 日期：2026-05-21
# 难度：Easy
# 题目：https://leetcode.com/problems/symmetric-tree/
# ============================================================
#
# 【思路】递归判断镜像对称
#
# 核心：判断左子树和右子树是否镜像
# 辅助函数 isMirror(left, right)：
#   - 当前节点值相同
#   - left.left 对应 right.right（交叉递归）
#   - left.right 对应 right.left（交叉递归）
#
# 与 #100 isSameTree 的区别：
#   #100：左对左，右对右
#   #101：左对右，右对左（交叉）
#
# 时间复杂度：O(n)  每个节点访问一次
# 空间复杂度：O(h)  h为树高，递归栈深度
# ============================================================

class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
