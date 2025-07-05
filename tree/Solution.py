# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 105 Construct Binary Tree from Preorder and Inorder Traversal
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))
            rootNode = TreeNode(inorder[index])
            rootNode.left = self.buildTree(preorder, inorder[0:index])
            rootNode.right = self.buildTree(preorder, inorder[index+1:])
            return rootNode
    

    # 637 Average of Levels in Binary Tree
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = [root]
        res = []
        while que:
            level = []
            for _ in range(len(que)):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                level.append(node.val)
            avg = sum(level) / len(level)
            res.append(avg)
        return res
    

    # 129 Sum Root to Leaf Numbers
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        path = []

        def traverse(root):
            if root == None:
                return
            if root.left == root.right == None:
                path.append(root.val)    
                res[0] += int("".join(map(str, path)))
                path.pop()
                return

            path.append(root.val)
            traverse(root.left)
            traverse(root.right)
            path.pop()

        traverse(root)
        return res[0]
    

    # 114 Flatten Binary Tree to Linked List
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return 
        if root.left:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            tmp.right = root.right
            root.right = root.left
        root.left = None
        self.flatten(root.right)

    
    # 102 Binary Tree Level Order Traversal
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res

        tmp = [root]
        while tmp:
            level = []
            for _ in range(len(tmp)):
                node = tmp.pop(0)
                level.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(level)
        return res
    

    # 103 Binary Tree Zigzag Level Order Traversal
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        tmp = [root]
        zigzag = False
        while tmp:
            level_size = len(tmp)
            level = [0] * level_size
            for i in range(len(tmp)):
                node = tmp.pop(0)
                if zigzag:
                    level[level_size-1-i] = node.val
                else:
                    level[i] = node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(level)
            zigzag = not zigzag
        return res
    

    # 230 Kth Smallest Element in a BST
    def __init__(self):
        self.cnt = 0
        self.res = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root):
            if not root or self.res is not None:
                return 
            inorder(root.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = root.val
                return 
            inorder(root.right)

        inorder(root)
        return self.res