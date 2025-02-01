class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def push(head, data):
    return Node(data, head)


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def sorted_merge(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result


def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list


def merge_two_sorted_lists(list1, list2):
    return sorted_merge(list1, list2)


def main():
    list1 = None
    for data in [70, 30, 50, 10]:
        list1 = push(list1, data)
    print("First list:")
    print_list(list1)

    list2 = None
    for data in [80, 20, 40, 60]:
        list2 = push(list2, data)
    print("\nSecond list:")
    print_list(list2)

    list1 = reverse_list(list1)
    print("\nFirst list after reversing:")
    print_list(list1)

    list1 = merge_sort(list1)
    list2 = merge_sort(list2)
    print("\nFirst list after sorting:")
    print_list(list1)
    print("\nSecond list after sorting:")
    print_list(list2)

    merged_list = merge_two_sorted_lists(list1, list2)
    print("\nMerged sorted list:")
    print_list(merged_list)


if __name__ == "__main__":
    main()
