from __future__ import annotations

import collections
from dataclasses import dataclass
from typing import Any
import yaml


@dataclass
#я не знаю в чем проблема и как это решить, но при использовании dataclass
#у меня ломается вывод, хотя функции и алгоритм в целом вроде нормальные
#поэтому я дополнительно переопределила init
class Node:
    def __init__(self, data = 0, left = None, right = None, key = Any):
        self.data = data
        self.key = key
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self, root: Node) -> list[Any]:
        if not root:
            return []

        answer = []
        reverse = False
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for node in q:
                if node.data is not None:
                    level.append(node.data)
            if reverse:
                answer.append(level[::-1])
            else:
                answer.append(level)
            nw_level = []
            for node in q:
                if node.left:
                    nw_level.append(node.left)
                if node.right:
                    nw_level.append(node.right)
            reverse = not reverse
            q = nw_level
        return answer

def build_tree(list_view: list[Any]) -> Node:
    if not list_view:
        return None
    root = Node(list_view[0])
    q = [root]
    i = 1
    while i < len(list_view):
        current_node = q.pop(0)
        if list_view[i] is not None:
            current_node.left = Node(list_view[i])
            q.append(current_node.left)
        i += 1
        if i < len(list_view) and list_view[i] is not None:
            current_node.right = (Node(list_view[i]))
            q.append(current_node.right)
        i += 1
    return root


if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open("C://Users//Alexandra//Documents//Универ//Algos//fundamentals-of-algorithms//practicum_5//homework//basic//binary_tree_zigzag_level_order_traversal_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = BinaryTree()
        bt.root = build_tree(c["input"])
        a = c["input"]
        print(a)
        zz_traversal = bt.zigzag_level_order_traversal(bt.root)
        print(zz_traversal)
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
