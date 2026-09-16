# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node , maxseen):
            if not node:
                return 0
            count = 0

            if node.val >= maxseen:
                count += 1

            maxseen = max(maxseen, node.val)

            count += dfs(node.left, maxseen)
            count += dfs(node.right, maxseen)

            return count

        return dfs(root, root.val)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna