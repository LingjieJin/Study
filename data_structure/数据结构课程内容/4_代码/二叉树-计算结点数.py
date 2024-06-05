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

###
###
###
# 计算二叉树结点数
def node_count(node):
    if not node:
        return 0
    
    return 1 + node_count(node.left) + node_count(node.right)
###
###
###

