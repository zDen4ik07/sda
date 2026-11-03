class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)

        if not root:
            return newNode

        cur = root
        parent = None

        
        while cur:
            parent = cur

            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        
        if val < parent.val:
            parent.left = newNode
        else:
            parent.right = newNode

        return root