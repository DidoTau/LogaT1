
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 
        self.height = 1
    
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
        return node 

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