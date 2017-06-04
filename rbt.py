from Node import Node
from Node import leafNode

class RBTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        tree = self.root
        while tree != None:
            if tree.val == key:
                return tree
            if tree.val > key:
                tree = tree.left
            else:
                tree = tree.left
        return None

    def minimum(self, tree):
        x = None
        while tree.left != None:
            x = tree.left
            tree = tree.left
        return x

    def transplant(self, tree, newtree):
        if tree.p == None:
            self.root = newtree
        elif tree == tree.p.left:
            tree.p.left = newtree
        else:
            tree.p.right = newtree
        if newtree != None:
            newtree.p = tree.p

    def leftRotate(self, tree, x):
        y = x.right

        x.right = y.left
        if y.left != None:
            y.left.p = x

        y.p = x.p
        if x.p == None:
            tree.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.parent = y

    def rightRotate(self, tree, x):
        y = x.left

        x.left = y.right
        if y.right != None:
            y.right.p = x

        y.p = x.p
        if x.p == None:
            tree.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.right = x
        x.parent = y
             
    def insert(self, key):
        new = Node(key)
        parent = None
        x = self.root 

        #find the node place for insertion
        while x != None and x.val != None:
            parent = x
            if x.val > new.val:
                x = x.left
            else:
                x = x.right

        #insert a key to a place
        new.p = parent

        if parent is None:
            self.root = new
        elif new.val < parent.val:
            parent.left = new
        else:
            parent.right = new

        #tree balancing하기
        self.RBT_insertFixup(tree, n) #

    def RBT_insertFixup(self, tree, n):
        while n.p != None and n.p.p != None and n.p.color == 'Red':
            if n.p == n.p.p.left:
                y = n.p.p.right
                if y != None and y.color == 'Red':
                    n.p.color = 'Black'
                    y.color = 'Black'
                    n.p.p.color = 'Red'
                    n = n.p.p
                else:
                    if n == n.p.right:
                        n = n.p
                        self.leftRotate(tree, n)
                    n.p.color = 'Black'
                    n.p.p.color = 'Red'
                    self.rightRotate(tree, n.p.p)
            else:
                y = n.p.p.left
                if y != None and y.color == 'Red':
                    n.p.color = 'Black'
                    y.color = 'Black'
                    n.p.p.color = 'Red'
                    n = n.p.p
                else:
                    if n == n.p.left:
                        n = n.p
                        self.rightRotate(tree, n)
                    n.p.color = 'Black'
                    n.p.p.color = 'Red'
                    self.leftRotate(tree, n.p.p) 
        self.root.color = 'Black'

    def delete(self, tree, n):
        target = self.search(n)
        if target == None:
            return

        y = target
        yOriginalColor = y.color

        if target.left.val == None:
            x = target.right
            self.transplant(target, target.right)

        elif target.right.val == None:
            x = target.left
            self.transplant(target, target.left)

        else:
            y = self.minimum(target.right)
            yOriginalColor = y. color
            x = y.right

            if y.p == target:
                x.p = target.right
            else:
                self.transplant(y, y.right)
                y.right = target.right
                y.right.p = y

            self.transplant(target, y)
            y.left = target.left
            y.left.p = y
            y.color = target.color

        if yOriginalColor == 'Black':
            self.RBT_deleteFixup(tree, x) #

    def RBT_deleteFixup(self, tree, x):
        while x != tree.root and x.color == 'Black':
            if x == x.p.left: # x at the left side
                w = x.p.right # x's sibling

                # case 1
                if w.color == 'Red':
                    w.color == 'Black'
                    x.p.color == 'Red'
                    self.leftRotate(tree, x.p)
                    w = x.p.right 

                # case 2
                if w.left.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.parent

                # case 3
                else:
                    if w.right.color == 'Black':
                        w.left.color = 'Black'
                        w.color = 'Red'
                        self.rightRotate(tree, w)
                        w = x.p.right

                    #case 4
                    w.color = x.p.color
                    x.p.color = 'Black'
                    w.right.color = 'Black'
                    self.leftRotate(tree, x.p)
                    x = tree.root

            else:
                w = x.p.left

                #case1
                if w.color == 'Red':
                    w.color == 'Black'
                    x.p.color == 'Red'
                    self.rightRotate(tree, x.p)
                    w = x.p.left 

                #case 2
                if w.left.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.parent

                #case 3
                else:
                    if w.leftt.color == 'Black':
                        w.right.color = 'Black'
                        w.color = 'Red'
                        self.leftRotate(tree, w)
                        w = x.p.left

                    #case 4
                    w.color = x.p.color
                    x.p.color = 'Black'
                    w.left.color = 'Black'
                    self.rightRotate(tree, x.p)
                    x = tree.root
        if x != None:
            x.color = 'Black'

    def print(self, tree, level):
        if tree.right is not None:
            self.print(tree.right,level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val)
        if tree.left is not None:
            self.print(tree.left, level + 1)

    def nodeCount(self, tree, node=0):
         
        if tree.val == None:
            return 0
        else:
            return self.nodeCount(tree.left) + self.nodeCount(tree.right) + 1

    def printTotalNode(self, tree):
        print(self.nodeCount(tree))

    def blackNodeCount(self, tree):
        if tree.val == None:
            return 0
        elif tree.color == 'Black':
            return self.blackNodeCount(tree.left) + self.blackNodeCount(tree.right) + 1
        else:
            return self.blackNodeCount(tree.left) + self.blackNodeCount(tree.right)

    def printBlackNumber(self, tree):
        print(self.blackNodeCount(tree)

    def inOrderTraversal(self, tree):
        if tree.left.val is not None:
            self.inOrderTraversal(tree.left)
        print(tree.val, end=" ")
        if tree.right.val is not None:
            self.inOrderTraversal(tree.right)

    def blackHeight(self, tree, n=0):
        if tree.val is None:
            return 0
        elif tree.color == 'Black':
            return self.blackHeight(tree.left) + 1
        else: 
            return self.blackHeight(tree.left)
        
    def printBlackHeight(self, tree, n = 0):
        print(self.blackHeight(tree, n))
