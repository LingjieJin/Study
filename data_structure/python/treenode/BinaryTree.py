from collections import deque

# 二叉树的存储 - 二叉链表
class BinaryTree:
    #1. 构造方法
    def __init__(self, newValue):
        self.key = newValue        # 树根
        self.left = None           # 左子树初始值为空
        self.right = None          # 右子树初始值为空

    #2. 访问左子树
    def getLeft(self):
        return self.left

    #3. 访问右子树
    def getRight(self):
        return self.right

    #4. 修改树根的值
    def setRoot(self, newValue):
        self.key = newValue

    #5. 访问树根
    def getRoot(self):
        return self.key
    
    # 使用前序遍历的队列
    @staticmethod
    def createBT(preorder:deque):
        if not preorder:
            return None

        value = preorder.popleft()
        ### 如果是空字符，返回
        if value == '#':
            return None

        node = BinaryTree(value)
        node.left = BinaryTree.createBT(preorder)
        node.right = BinaryTree.createBT(preorder)

        return node
    
    ## 前序遍历
    @staticmethod
    def preOrder(root):
        if not root:
            return
        print(root.getRoot(), end=" ")
        BinaryTree.preOrder(root.getLeft())
        BinaryTree.preOrder(root.getRight())
        
    ## 中序遍历
    @staticmethod
    def inOrder(root):
        if not root:
            return
        BinaryTree.inOrder(root.getLeft())
        print(root.getRoot(), end=" ")
        BinaryTree.inOrder(root.getRight())
        
    
    ## 后序遍历
    @staticmethod
    def postOrder(root):
        if not root:
            return
        BinaryTree.postOrder(root.getLeft())
        BinaryTree.postOrder(root.getRight())
        print(root.getRoot(), end=" ")
    
   
if __name__ == '__main__':
    a = "ABD##E##CF##G##"
    q = deque()
    for x in a:
        q.append(x)

    bt = BinaryTree.createBT(q)

    BinaryTree.preOrder(bt)
    print()
    BinaryTree.midOrder(bt)
    print()
    BinaryTree.postOrder(bt)
    print()