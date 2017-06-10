from Node_fix import Node
from Tree_fix import RBT

def main():
    # open the file to get numbers 
    data = []

    f = open("input.txt", 'r')
    lines = f.readlines()
    for line in lines:
        inputNumber = int(line.strip())
        data.append(inputNumber)
    
    f.close()

    rbt = RBT()
    
    #read data for input 
    for i in data:
        if i > 0:
            rbt.insert(i)
        elif i < 0:
            rbt.delete(-i)
        else:
            break
    # rbt.print(rbt.root, 0)
    
    rbt.printTotalNode(rbt.root)

    rbt.printBlackNode(rbt.root)

    rbt.printBlackHeight(rbt.root)

    print("Inorder Traversal: ")
    rbt.inOrderTraversal(rbt.root)

main()
