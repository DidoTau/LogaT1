from Node import *
# AVL tree class which supports the
# Insert operation
class AVL(Node):
    def __init__(self):
        super().__init__(val = 0)
 
    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, node, key):

        # insercion normal en clase Node
        node = super().insert(node, key)
 
        # actualiza la altura del nodo luego de la insercion
        self.updateHeight(node)
        # retorna arbol balanceado    
        return self.balance(node, key)

    def balance(self, node, key):
        # calcula el balance del arbol
        balance = self.getBalance(node)
 
        # si el arbol no está balanceado
        # desbalance Left Left
        if balance > 1 and key < node.left.val:
            return self.rightRotate(node)
 
        # desbalance Right Right
        if balance < -1 and key > node.right.val:
            return self.leftRotate(node)
 
        # desbalance - Left Right
        if balance > 1 and key > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
 
        # desbalance - Right Left
        if balance < -1 and key < node.right.val:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)  
        return node
    def updateHeight(self, node):
        node.height = 1 + max(super().getHeight(node.left),
                           super().getHeight(node.right))
    def search(self, node, key):
        current = node 
        while node:
            if(current.val == key):               
                break
            current = current.right if current.val < key else current.left
        return current
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
        # rotacion
        y.left = z
        z.right = T2

        # actualiza alturas luego de rotar
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root):
     
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
# Driver program to test above function
myTree = AVL()
root = None
 
root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)
 
"""The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""
 
# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
myTree.preOrder(root)
print()
print("buscando: ",myTree.search(root, 25))