import sys

class Node:
    def __init__(self, _data):
        self.data = _data
        self.left = None
        self.right = None
        self.left_w = None
        self.right_w = None

    def __str__(self):
        return str(self.data)

def pre(_node):
    print(_node, end = '')
    if not _node.left == None :
        pre(tree[_node.left])
    if not _node.right == None :
        pre(tree[_node.right])
    
n = int(sys.stdin.readline())

tree = {}
childcheck = [0 for i in range(n + 1)]

for i in range(n - 1):
    d1, d2, w = map(str, sys.stdin.readline().split())
    
    tree[d1] = Node(d1) 
    tree[d2] = Node(d2)
    
    if childcheck[int(d1)] == 0:
        tree[d1].left = tree[d2]
        tree[d1].left_w = w
        childcheck[int(d1)] = 1
    else:
        tree[d1].right = tree[d2]
        tree[d1].right_w = w
        childcheck[int(d1)] = 2
        
        
pre(tree['1'])