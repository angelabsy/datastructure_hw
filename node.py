class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = leafNode()
        self.right = leafNode()
        self.p = None
        self.color = 'Red'


class leafNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.p = None
        self.color = 'Black'
