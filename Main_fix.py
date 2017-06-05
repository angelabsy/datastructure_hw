from Node import Node
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
    rbt.print(rbt.root, 0)
    
    print("Number of Total Node")
    rbt.printTotalNode(rbt.root)

    print("Number of Black Node")
    rbt.printBlackNode(rbt.root)

    print("Black Height")
    rbt.printBlackHeight(rbt.root)

    print("Inorder Traversal")
    rbt.inOrderTraversal(rbt.root)

main()
