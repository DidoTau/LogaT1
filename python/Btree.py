class NodoB:
    def __init__(self, hoja=False):
        self.esHoja = hoja
        self.valores = []
        self.hijos = []

    def search(self,val ,nodo):
        largo = len(nodo.valores)
        arr = nodo.valores
        for i in range(largo):
            if val == arr[i]:
                return True
            elif val < arr[i] and nodo.esHoja == True :
                return False
            elif val < arr[i] :
                return self.search(val,nodo.hijos[i])   
            elif val > arr[i] and len(nodo.valores) == i+1 :
                if nodo.esHoja == True :
                    return False
                else: 
                    return self.search(val,nodo.hijos[i+1]) 



class Btree:
    def __init__(self, b):
        self.raiz = NodoB(True)
        self.B = b

    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.valores), end=":")
        for i in x.valores:
            print(i, end=" ")
        print()
        l += 1
        if len(x.hijos) > 0:
            for i in x.hijos:
                self.print_tree(i, l)
            

    def insert(self, val):
        B = self.B
        raiz = self.raiz

        if len(raiz.valores) < B: #si no esta llena la raiz
            self.insertarNoLlena(raiz, val)
        
        else: #si l araiz está llena la parimos
            nuevaRaiz = NodoB()    #creamos nodo que sera la nueva raiz
            self.raiz = nuevaRaiz
            nuevaRaiz.hijos.insert(0, raiz)  #la nueva raiz  su primer hijo sera la ex raiz
            self.partir(nuevaRaiz, 0)  
            self.insertarNoLlena(nuevaRaiz, val) #luego recien insertamos el valor
        


    
    def partir(self, raizNueva, pos):
        B = self.B
        nodoLleno = raizNueva.hijos[pos]
        nodoAyuda = NodoB(nodoLleno.esHoja)  #nodo con el que el nodo que esta lleno comparte sus cosas
        raizNueva.hijos.insert(pos + 1, nodoAyuda) #inserta el nuevo noso como un hijo al arreglo de nodos 
        
        raizNueva.valores.insert(pos, nodoLleno.valores[int((B-1)/2)])  # insertamos el valor del nueevo 
        for i in range(int((B+1)/2),B):  #nuval del nod
            nodoAyuda.valores.append(nodoLleno.valores[i])
        #print("nodod ayuda",nodoAyuda.valores)
        #print("nodo lleno",nodoLleno.valores) 
        lista = []   
        for j in range(0, int((B-1)/2)): #cambiamos val de nodo lleno
            lista.append(nodoLleno.valores[j])
        nodoLleno.valores = lista 
        #print("nodo lleno " , nodoLleno.valores)    
        #nodoAyuda.valores = nodoLleno.valores[int((B+1)/2): B]  #le pasamos loso valores
        #nodoLleno.valores = nodoLleno.valores[0: int((B-1)/2)]
        
        if not nodoLleno.esHoja: #si el que se lleno no era una hoja tenemos que a los otros tamboen pasarle sus hijos nodos
            for i in range(int((B+1)/2),B+1):  #insertamso los hijos al nuevo nodo
                nodoAyuda.hijos.append(nodoLleno.hijos[i])   
            listah = []    
            for j in range(0, int((B-1)/2)):   #cambiamos los hijpos del nodo lleno
                listah.append(nodoLleno.hijos[j])
            nodoLleno.hijos = listah       
           # nodoAyuda.hijos = nodoLleno.hijos[int((B+1)/2) : B+1 ]
           # nodoLleno.hijos = nodoLleno.hijos[0: int((B-1)/2)]


            
    

    def insertarNoLlena(self, raiz, val):
        B = self.B         
        pos = len(raiz.valores) - 1

        if raiz.esHoja:   #si es una hoja podemos inssertar aca
            raiz.valores.append(None) 
            while pos >= 0 and val < raiz.valores[pos]:   #movemos una posicion los valores hasta que corresponda ingresar el nuevp
                raiz.valores[pos + 1] = raiz.valores[pos]
                pos -= 1
            raiz.valores[pos + 1] = val    #ingresamos el nuevo
        else:    #si no es una hoja 
            while pos >= 0 and val < raiz.valores[pos]:
                pos -= 1
            pos += 1

            if len(raiz.hijos[pos].valores) == B:
                self.partir(raiz, pos)
                if val > raiz.valores[pos]:
                    pos += 1
            self.insertarNoLlena(raiz.hijos[pos], val)

    def reset(self):
        self.raiz = NodoB(True)
        self.B = self.B
            


    def search(self,val):
        return self.raiz.search(val ,self.raiz)