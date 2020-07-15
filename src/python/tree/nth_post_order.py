# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def posrOrderTravarsal(node: Node):

    if node.left is not None:
        posrOrderTravarsal(node.left)

    if node.right is not None:
        posrOrderTravarsal(node.right)
    
    print(node.val, end=' ')


count = 0
def getNtPostorder(node, n):
    global count
    if node is None:
        return
    
    if count < n: 
        getNtPostorder(node.left, n)
        
        getNtPostorder(node.right, n)

        count += 1
        if count == n:
            print(n, 'th node is: ', node.val)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)  
    root.right = Node(30)  
    root.left.left = Node(40)  
    root.left.right = Node(50)

    
    
    posrOrderTravarsal(root)
    print('\n')
    n = 4
    getNtPostorder(root, n)
    
