import sys

class Node:
    def __init__(self, _data, _left, _right):
        self.data = _data
        self.left = _left
        self.right = _right

    def __str__(self):
        return str(self.data)
        
    
def pre_order_traversal(_node):
    print(_node, end = '')
    if not _node.left == "." :
        pre_order_traversal(tree[_node.left])
    if not _node.right == "." :
        pre_order_traversal(tree[_node.right])

def in_order_traversal(_node):
    if not _node.left == "." :
        in_order_traversal(tree[_node.left])
    print(_node, end = '')
    if not _node.right == "." :
        in_order_traversal(tree[_node.right])

def post_order_traversal(_node):
    if not _node.left == "." :
        post_order_traversal(tree[_node.left])
    if not _node.right == "." :
        post_order_traversal(tree[_node.right])
    print(_node, end = '')
        
n = int(sys.stdin.readline())

tree = {}

for i in range(n):
    d1, d2, d3 = map(str, sys.stdin.readline().split())
    tree[d1] = Node(d1, d2, d3)

pre_order_traversal(tree['A'])
print()
in_order_traversal(tree['A'])
print()
post_order_traversal(tree['A'])