import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

# Функція для додавання ребер до графа (для NetworkX)
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо поточний вузол до графа з його кольором та міткою (значенням)
        graph.add_node(node.id, color=node.color, label=node.val)
        
        # Якщо є лівий нащадок, додаємо ребро і рекурсивно обробляємо піддерево
        if node.left:
            graph.add_edge(node.id, node.left.id)
            new_x_left = x - 1 / 2 ** layer
            pos[node.left.id] = (new_x_left, y - 1)
            add_edges(graph, node.left, pos, x=new_x_left, y=y - 1, layer=layer + 1)
        
        # Якщо є правий нащадок, додаємо ребро і рекурсивно обробляємо піддерево
        if node.right:
            graph.add_edge(node.id, node.right.id)
            new_x_right = x + 1 / 2 ** layer
            pos[node.right.id] = (new_x_right, y - 1)
            add_edges(graph, node.right, pos, x=new_x_right, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Отримуємо список кольорів та міток вузлів
    colors = [data['color'] for node_id, data in tree.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# --- Побудова дерева з купи ---

# Функція для побудови бінарного дерева із купи (списку)
def build_heap_tree(heap, index=0):
    if index < len(heap):
        # Створюємо вузол із поточним значенням
        node = Node(heap[index])
        # Рекурсивно створюємо ліве та праве піддерева
        node.left = build_heap_tree(heap, 2 * index + 1)
        node.right = build_heap_tree(heap, 2 * index + 2)
        return node
    return None

# Функція для візуалізації бінарної купи
def draw_heap(heap):
    root = build_heap_tree(heap)
    draw_tree(root)

# --- Приклад використання ---

if __name__ == "__main__":
    # Приклад бінарної купи, представлений як список
    heap = [0, 4, 1, 5, 10, 3]
    draw_heap(heap)
