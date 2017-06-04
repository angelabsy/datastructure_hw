from node import Node
from rbt import RBTree

data = []

f = open("input.txt", 'r')
lines = f.readlines()
for line in lines:
    inputNumber = int(line.strip())
    data.append(inputNumber)
    
f.close()

def main():

    rbt = RBTree()
    
    for i in data:
        if i > 0:
            rbt.insert(rbt.root, i)
        elif i < 0:
            rbt.delete(rbt.root, -i)
        else:
            break

    print ('Number of Total Node: ')
    rbt.printTotalNumber(rbt.root)

    print ('Number of Black Node: ')
    rbt.printBlackNumber(rbt.root)

    print ('Black Height: ')
    rbt.printBlackHeight(rbt.root)

    print ('Inorder Traversal: ')
    rbt.inOrderTraversal(rbt.root)


main()
