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

###
###
###
