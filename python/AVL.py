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

    def leftRotate(self, node):
 
        node_r = node.right
        node_r_l = node_r.left
        # rotacion
        node_r.left = node
        node.right = node_r_l

        # actualizo las alturas luego de rotar
        node.height = 1 + max(self.getHeight(node.left),
                         self.getHeight(node.right))
        node_r.height = 1 + max(self.getHeight(node_r.left),
                         self.getHeight(node_r.right))
 
        # Return the new root
        return node_r
 
    def rightRotate(self, node):
 
        node_l = node.left
        node_l_r = node_l.right
 
        # Perform rotation
        node_l.right = node
        node.left = node_l_r
 
        # Update heights
        node.height = 1 + max(self.getHeight(node.left),
                        self.getHeight(node.right))
        node_l.height = 1 + max(self.getHeight(node_l.left),
                        self.getHeight(node_l.right))
 
        # Return the new root
        return node_l
 
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
