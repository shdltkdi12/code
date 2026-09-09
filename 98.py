# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # first traversal to set rightmost child's right as root
        prev = root
        if prev.left:
            while True:
                print(prev.val)
                if not prev.left and not prev.right:
                    prev.right = root
                    break
                if not prev.left:
                    prev = prev.right
                if prev.left:
                    prev = prev.left
                
            
            # second traversal to check ascending order
            prev = root
            while prev:
                if not prev.left:
                    curr = prev.right
                else:
                    curr = prev.left

                if curr == root:
                    root.left = None
                    break
                if not curr.val < prev.val:
                    print('dbg1')
                    return False
                prev = curr

        while prev:
            if not prev.left and not prev.right:
                break
            if not prev.left:
                curr = prev.right
            else:
                curr = prev.left
            if prev == curr:
                break
            if not prev.val < curr.val:
                print('dbg2')
                return False
            prev = curr
        return True


