import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Клас вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Початковий колір (за замовчуванням "skyblue")
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

# Функція для додавання ребер до графа (для NetworkX)
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо поточний вузол із його кольором та міткою (значенням)
        graph.add_node(node.id, color=node.color, label=node.val)
        
        # Якщо є лівий нащадок, додаємо ребро та рекурсивно обробляємо піддерево
        if node.left:
            graph.add_edge(node.id, node.left.id)
            new_x_left = x - 1 / 2 ** layer
            pos[node.left.id] = (new_x_left, y - 1)
            add_edges(graph, node.left, pos, x=new_x_left, y=y - 1, layer=layer + 1)
        
        # Якщо є правий нащадок, додаємо ребро та рекурсивно обробляємо піддерево
        if node.right:
            graph.add_edge(node.id, node.right.id)
            new_x_right = x + 1 / 2 ** layer
            pos[node.right.id] = (new_x_right, y - 1)
            add_edges(graph, node.right, pos, x=new_x_right, y=y - 1, layer=layer + 1)
    return graph

# Модифікована функція для візуалізації дерева з можливістю анімації
def draw_tree(tree_root, algorithm_name=None):
    plt.clf()  # Очищуємо поточну фігуру
    
    # Якщо передано назву алгоритму, встановлюємо її як назву вікна
    if algorithm_name:
        plt.gcf().canvas.manager.set_window_title(algorithm_name)
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    # Отримуємо список кольорів та міток вузлів
    colors = [data['color'] for node_id, data in tree.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}
    
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.draw()
    plt.pause(1)  # Пауза для спостереження за змінами

# Функція для підрахунку кількості вузлів (ітеративно)
def count_nodes(root):
    if not root:
        return 0
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        count += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count

# Функція для генерації кольору у 16-річному форматі за заданим порядком
# Ми інтерполюємо від темного до світлого відтінку
def get_color(order, total, start_color=(0, 0, 139), end_color=(173, 216, 230)):
    """
    start_color – темний відтінок (наприклад, "darkblue": (0, 0, 139))
    end_color – світлий відтінок (наприклад, "lightblue": (173, 216, 230))
    """
    if total <= 1:
        return f'#{start_color[0]:02X}{start_color[1]:02X}{start_color[2]:02X}'
    t = order / (total - 1)
    R = int(start_color[0] + (end_color[0] - start_color[0]) * t)
    G = int(start_color[1] + (end_color[1] - start_color[1]) * t)
    B = int(start_color[2] + (end_color[2] - start_color[2]) * t)
    return f'#{R:02X}{G:02X}{B:02X}'

# Обхід у глибину (DFS) із використанням стека (без рекурсії)
def dfs_traversal(root):
    total = count_nodes(root)  # Загальна кількість вузлів
    order = 0  # Лічильник порядку відвідування
    stack = [root]
    
    while stack:
        node = stack.pop()
        # Оновлюємо колір вузла згідно з порядком відвідування
        node.color = get_color(order, total)
        order += 1
        
        # Візуалізуємо поточний стан дерева
        draw_tree(root, algorithm_name="DFS Traversal")
        
        # Додаємо дітей у стек: спочатку правого, потім лівого,
        # щоб лівий вузол оброблявся першим (типовий pre-order обхід)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Обхід у ширину (BFS) із використанням черги (без рекурсії)
def bfs_traversal(root):
    total = count_nodes(root)  # Загальна кількість вузлів
    order = 0  # Лічильник порядку відвідування
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        node.color = get_color(order, total)
        order += 1
        
        draw_tree(root, algorithm_name="BFS Traversal")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Функція для скидання кольорів вузлів до початкового значення (без рекурсії)
def reset_tree_colors(root, default_color="skyblue"):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        node.color = default_color
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Головна функція
def main():
    # Створюємо приклад бінарного дерева
    #           A
    #         /   \
    #        B     C
    #       / \   / \
    #      D   E F   G
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.left = Node("F")
    root.right.right = Node("G")
    
    plt.ion()  # Увімкнення інтерактивного режиму для анімації

    print("Обхід у глибину (DFS):")
    dfs_traversal(root)
    plt.pause(1)  # Пауза після завершення обходу DFS

    # Скидання кольорів для наступного обходу
    reset_tree_colors(root)
    draw_tree(root)  # Відобразити початковий стан дерева
    plt.pause(1)

    print("Обхід у ширину (BFS):")
    bfs_traversal(root)
    plt.pause(1)
    
    plt.ioff()  # Вимикаємо інтерактивний режим
    plt.show()

if __name__ == "__main__":
    main()
