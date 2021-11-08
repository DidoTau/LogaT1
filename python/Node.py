
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 
        self.height = 1
        self.parent = None
        
    def insert(self, node, key):
        """
        Inserción clásica en un árbol binario

        Args:
            node ([type]): [description]
            key ([type]): [description]

        Returns:
            [type]: [description]
        """
        if not node: 
            return Node(key)
        elif key < node.val:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        

    def getHeight(self, node):    
        """
        Calcula la altura de un nodo dado

        Args:
            root ([type]): [description]

        Returns:
            [type]: [description]
        """
        if not node:
            return 0
        
        return node.height
    def search(self, node, key):
        
        while node:
            if(node.val == key):               
                return True
            return self.search(node.right, key) if node.val < key else self.search(node.left, key)
        return False