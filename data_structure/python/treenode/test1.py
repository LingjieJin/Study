from BTree import *

# 示例输入
preorder1 = ['A', 'B', 'D', '#', '#', 'E', '#', '#', 'C', 'F', '#', '#', 'G', '#', '#']
tree1 = build_tree(preorder1)

print("先序遍历:")
preorder_traversal(tree1)
print("\n中序遍历:")
inorder_traversal(tree1)
print("\n后序遍历:")
postorder_traversal(tree1)
print("\n层次遍历:")
print(level_order_traversal(tree1))
print("\n\n树的高度:", tree_height(tree1))
print("树的叶子数:", leaf_count(tree1))
print("树的结点数:", node_count(tree1))
