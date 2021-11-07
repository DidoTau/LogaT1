class Node:
    def __init__(self,val,izquierdo=None,derecho=None):
        self.value = val
        self.left = izquierdo
        self.right = derecho

    def insert(self ,val , nodeNow):
        if val < nodeNow.value:  
            if nodeNow.left == None:
                nodeNow.left = Node(val)
            else:
                self.insert(val, nodeNow.left)    
        else:  #val > nodeNow.val
            if nodeNow.right == None:
                nodeNow.right = Node(val)
            else:
                self.insert(val, nodeNow.right)

    def search(self, val, nodeNow):
        if nodeNow is None:
            return False
        elif val == nodeNow.value:
            return True
        else:
            if val < nodeNow.value:
                return self.search(val, nodeNow.left)
            else: #val > nodeNow.val
                return self.search(val,nodeNow.right)


class ABB:
    def __init__(self) -> None:
        self.root = None    

    def insert(self,val):
        if self.root == None:
            self.root = Node(val=val)   
        else:
            self.root.insert(val, self.root) 

    def search(self,val):
        if self.root == None:
            return False
        else:
            return self.root.search(val, self.root)                   



