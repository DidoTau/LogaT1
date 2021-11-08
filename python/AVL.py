from Node import *
# AVL tree class which supports the
# Insert operation
class AVL(Node):
    def __init__(self):
        self.root = None
 

    def insert(self, key):

        # insercion normal en clase Node
        if self.root == None:
            self.root = Node(val=key)
        else:
            self.root.insert(self.root, key)
 
        # actualiza la altura del nodo luego de la insercion
        self.updateHeight(self.root)
        # retorna arbol balanceado    
        self.balance(key)

    def balance(self, key):
        # calcula el balance del arbol
        balance = self.getBalance(self.root)
 
        # si el arbol no está balanceado
        # desbalance Left Left
        if balance > 1 and key < self.root.left.val:
            return self.rightRotate(self.root)
 
        # desbalance Right Right
        if balance < -1 and key > self.root.right.val:
            return self.leftRotate(self.root)
 
        # desbalance - Left Right
        if balance > 1 and key > self.root.left.val:
            self.root.left = self.leftRotate(self.root.left)
            return self.rightRotate(self.root)
 
        # desbalance - Right Left
        if balance < -1 and key < self.root.right.val:
            self.root.right = self.rightRotate(self.root.right)
            return self.leftRotate(self.root)  
        return self.root
    def updateHeight(self, node):
        node.height = 1 + max(super().getHeight(node.left),
                           super().getHeight(node.right))
    def search(self, key):
        if self.root == None:
            return False
        else: 
            return self.root.search(self.root, key)

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
    def reset(self):
        self.root = None
