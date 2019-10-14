class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class AdlistImp:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.prev = None
        self.head.tail = self.tail
        self.tail.prev = self.head
        self.tail.tail = None

        self.len = 0

    def push(self, val):
        new_node = Node(val)
        if self.len == 0:
            new_node.prev = self.head
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.next = self.tail
        else:
            pre_node = self.tail.prev
            pre_node.next = new_node
            new_node.prev = pre_node
        new_node.next = self.tail
        self.tail.prev = new_node
        self.len += 1

    def pop(self):
        if self.len != 0:
            preNode = self.tail.prev
            pop_value = preNode.value
            ppreNode = preNode.prev
            ppreNode.next = self.tail
            self.tail.pre = ppreNode
        else:
            pop_value = None
        self.len -= 1
        return pop_value

    def shift(self):
        if self.len != 0:
            nextNode = self.head.next
            shift_value = nextNode.value
            nnextNode = nextNode.next
            nnextNode.prev = self.head
            self.head.next = nnextNode
        else:
            shift_value = None
        self.len -= 1
        return shift_value

    def unshift(self, val):
        new_node = Node(val)
        if self.len == 0:
            new_node.prev = self.head
            self.head.next = new_node

            new_node.next = self.tail
            self.tail.prev = new_node
        else:
            next_node = self.head.next
            new_node.prev = self.head
            self.head.next = new_node

            new_node.next = next_node
            next_node.prev = new_node
        self.len += 1

    # 释放节点
    def length(self):
        return self.len
