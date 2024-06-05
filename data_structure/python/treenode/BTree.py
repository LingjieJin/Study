## 树节点结构
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

## 二叉树的构造
## 根据前序队列构造二叉树
def build_tree(preorder):
    if not preorder:
        return None

    value = preorder.pop(0)
    ### 如果是空字符，返回
    if value == '#':
        return None

    node = TreeNode(value)
    node.left = build_tree(preorder)
    node.right = build_tree(preorder)

    return node

## 先序遍历
## 根节点 -> 左子树 -> 右子树
def preorder_traversal(node):
    if not node:
        return
    print(node.value, end=' ')
    preorder_traversal(node.left)
    preorder_traversal(node.right)

## 先序遍历 迭代法
def preorder_traversal_iter(root):
    if not root:
        return []
    
    result = []
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.value)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

## 中序遍历
## 左子树 -> 根节点 -> 右子树
def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.value, end=' ')
    inorder_traversal(node.right)

## 中序遍历 迭代
def inorder_traversal_iter(root):
    if not root:
        return []
    
    result = []
    stack = []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.value)
        current = current.right
    
    return result

## 后序遍历
## 左子树 -> 右子树 -> 根节点
def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value, end=' ')

## 后续遍历 迭代
def postorder_traversal_iter(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.insert(0, node.value)
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result

## 层次遍历
## 首先判断根节点是否为空，如果为空则返回空列表。
## 初始化一个空列表 result 用于存储遍历结果，以及一个队列 queue 用于辅助层次遍历。
## 将根节点 root 添加到队列 queue 中。
## 进入循环，只要队列不为空，就继续进行遍历。
## 在每一层遍历开始前，记录当前层的结点个数 level_size 和一个空列表 level_values 用于存储当前层的结点值。
## 在内层循环中，遍历当前层的所有结点，依次从队列中弹出一个结点，并将其值添加到 level_values 中。
## 如果当前结点有左子结点，将左子结点添加到队列中；如果有右子结点，将右子结点添加到队列中。
## 遍历完当前层的所有结点后，将 level_values 添加到 result 中，表示当前层的遍历结果。
## 继续下一层的遍历，直到所有结点都被遍历完。
## 最后返回 result，即为二叉树的层次遍历结果。
def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        level_values = []

        for _ in range(level_size):
            node = queue.pop(0)
            
            level_values.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_values)

    return result

# 计算二叉树高度
def tree_height(node):
    if not node:
        return 0
    ## 左右子树中选一个最大的值
    return 1 + max(tree_height(node.left), tree_height(node.right))

# 计算二叉树叶子数
## 通过递归的方式计算每隔节点的叶子树
def leaf_count(node):
    if not node:
        return 0
    
    if not node.left and not node.right:
        return 1
    
    return leaf_count(node.left) + leaf_count(node.right)

# 计算二叉树结点数
def node_count(node):
    if not node:
        return 0
    
    return 1 + node_count(node.left) + node_count(node.right)


