from BTree import *

preorder2 = ['A', 'B', 'D', '#', '#','E','H','#', '#','I','#', '#', 'C', 'F', '#', '#', 'G','#', '#']
tree2 = build_tree(preorder2)

print("先序遍历:")
preorder_traversal(tree2)
print("\n中序遍历:")
inorder_traversal(tree2)
print("\n后序遍历:")
postorder_traversal(tree2)
print("\n层次遍历:")
print(level_order_traversal(tree2))
print("\n\n树的高度:", tree_height(tree2))
print("树的叶子数:", leaf_count(tree2))
print("树的结点数:", node_count(tree2))