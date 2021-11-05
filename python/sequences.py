import numpy as np 



def generateOperation():
    """
    Genera una operacion al azar

    """
    random_int = np.random.randint(low = 0, high = 100)
    if 0<random_int & random_int<50 :
        return 0                     #insertar
    elif 50<random_int & random_int<83:
        return 1                      #busqueda buena
    else:
        return 2                      #busqueda mala

def generateOperationArray(ops: int):
    """
    Genera un millon de operaciones

    Args:
        ops (int): [description]
    """
    ops_array =np.zeros(ops)   #10^6        
    for i in range(ops):
        ops_array[i] = generateOperation()    #llenamos arreglo con la op
    return ops_array

def operator(node, val, op, arr):
    """
    Realiza operación segun valor obtenido

    Args:
        node : arbol tipo nodo
        val : valor a agregar 
        op ([type]): [description]
    """
    if op == 0:                
        node.insert(val)
        arr[op]=1
        ##
    elif op==1:
        node.search(val)
    else:
        node.search(val)

def random(node, op, arr, n):
    """
    Genera números aleatorios para hacer operaciones
    en un árbol dado.
    Antes de realizar una operación, verifica si el valor
    fue o no insertado en el arreglo.

    Args:
        node ([type]): [description]
        op ([type]): [description]
        arr ([type]): [description]
        n ([type]): [description]
    """
    random_int = np.random.randint(low = 0, high = n)
    if op == 0 | op == 2:                            #si insercion o busqueda mala
        while arr[random_int] == 1:                  #mientras este en el arreglo
            random_int = np.random.randint(low = 0, high = n)       #generamos otro
        operator(node, random_int, op, arr)
    elif op ==1:                                     #si es busqueda buena
        while arr[random_int] == 0:                   #mientras no est en el arreglo
            random_int =  np.random.randint(low = 0, high = n)   #generamo otro
        operator(node, random_int, op, arr)

def increasing(node,op, arr, n, k, m):
    """
    Genera numeros que tienden a ser creciente para insertar pero q onda con los otros???????

    Args:
        node ([type]): [description]
        op ([type]): [description]
        arr ([type]): [description]
        n ([type]): [description]
    """
    random_int = np.random.randint(low = 0, high = k+m+1)  
    if op == 0 | op == 2:                            #si insercion o busqueda mala
        while arr[random_int] == 1:                  #mientras este en el arreglo
            random_int = np.random.randint(low = 0, high = k+m+1)       #generamos otro
        operator(node, random_int, op, arr)   # hacer update de m en las inserciones!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif op ==1:                                     #si es busqueda buena
        while arr[random_int] == 0:                   #mientras no est en el arreglo
            random_int =  np.random.randint(low = 0, high = k+m+1)   #generamoh otro
        operator(node, random_int, op, arr)

def biased(node, op, arr, n, k, m, f, P):
    """
    Funciona igual que random, pero al hacer búsquedas 
    exitosas elige los valores según la probabilidad
    con que fue ingresada

    Args:
        node ([type]): [description]
        op ([type]): [description]
        arr ([type]): [description]
        n ([type]): [description]
        k ([type]): [description]
        m ([type]): [description]
    """
    
    if op == 0 | op == 2:
        random_int = np.random.randint(low = 0, high = n)     # si insercion o busqueda mala
        while arr[random_int] != 0:                  # mientras este en el arreglo
            random_int = np.random.randint(low = 0, high = n)       # generamos otro
        operator(node, random_int, op, arr)
        arr[random_int] = f(random_int)/P  # ACTUALIZAR P !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif op ==1:
          
        random_int = np.random.choice(np.arange(n), arr)     # si es busqueda buena
        while arr[random_int] == 0:                   # mientras no est en el arreglo
            random_int =  np.random.randint(low = 0, high = n)   # generamos otro
        operator(node, random_int, op, arr)

def sequence(node, sec, n, subsample, sequence_type):
    """
    Genera sec secuencias de n operaciones cada una
    y guarda el tiempo de CPU / user time en un arreglo
    que es retornado al final.


    Args:
        node ([type]): [description]
        sec ([type]): [description]
        n ([type]): [description]
        subsample ([type]): [description]

    Returns:
    numpy.random.choice(numpy.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])
        [type]: [description]
    """
    times = np.zeros(int(n /subsample))       #valores tiempos c/ 1000 operaciones
    if sequence_type =="random":
        for i in range(sec): #100 
            arr_values = np.zeros(n)
            for j in range(n):               #recorremos el arreglo de operaciones?
                op = array_ops[j]        
                random(node, op, arr_values)
    elif sequence_type == "increasing":
        for i in range(sec): #100 
            arr_values = np.zeros(k+m)
            for j in range(n):               #recorremos el arreglo de operaciones?
                op = array_ops[j]   
                increasing(node, op, arr_values)
    elif sequence_type == "biased":
        for i in range(sec): #100 
            arr_values = np.zeros(n)
            for j in range(n):               #recorremos el arreglo de operaciones?
                op = array_ops[j]   
                biased(node, op, arr_values)
        #se supone q aqui ponemos la cuestio de los tiempos    
    return times


if __name__ == '__main__':
    n = int(10^2)
    array_ops  =  generateOperationArray(n)

