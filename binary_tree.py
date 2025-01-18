import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current.val

def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.val

def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)


def plot_tree(node, x=0, y=0, level=1, dx=1, ax=None):
    if node is None:
        return

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_aspect('equal')
        ax.axis('off')

   
    ax.scatter(x, y, s=200, c='skyblue', edgecolors='black', zorder=2)
    ax.text(x, y, str(node.val), ha='center', va='center', zorder=3)

  
    if node.left:
        ax.plot([x, x - dx], [y, y - 1], c='black', zorder=1)
        plot_tree(node.left, x - dx, y - 1, level + 1, dx / 2, ax)

   
    if node.right:
        ax.plot([x, x + dx], [y, y - 1], c='black', zorder=1)
        plot_tree(node.right, x + dx, y - 1, level + 1, dx / 2, ax)


root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

fig, ax = plt.subplots(figsize=(8, 6))
plot_tree(root, ax=ax)
plt.show()

print("Найбільше значення у дереві:", find_max(root))

print("Найменше значення у дереві:", find_min(root))

print("Сума всіх значень у дереві:", sum_tree(root))


