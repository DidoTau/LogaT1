import numpy as np 
import time
import matplotlib.pyplot as plt
from ABB import *

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
        arr[int(op)]=1
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
    if op == 0 or op == 2:                            #si insercion o busqueda mala
        while arr[random_int] == 1:                  #mientras esté en el arreglo
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
    
    if op == 0 or op == 2:
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
    Genera #sec secuencias de n operaciones cada una
    y guarda el tiempo de CPU / user time en un arreglo
    que es retornado al final.


    Args:
        node ([type]): [description]
        sec ([type]): [description]
        n ([type]): [description]
        subsample ([type]): [description]

    Returns:
 
        [type]: [description]
    """
    times = []   #valores tiempos c/ 1000 operaciones
    if sequence_type =="random":
        for i in range(sec): #100 
            arr_values = np.zeros(n) # existencia  de valores
            arr_values[0] = 1 # 0 existe
            times_i = []
            start_time = time.process_time()
            for j in range(n):               #recorremos el arreglo de operaciones?
                op = array_ops[j]        
                random(node, op, arr_values, n)
                if (j+1)%subsample == 0 and j !=0: # cada mil ca
                    times_i.append(time.process_time()- start_time)
            times.append(times_i)    
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

def results(m):
    """[summary]

    Args:
        m ([type]): [description]

    Returns:
        [type]: [description]
    """
    m = np.array(m)
    mean =  m.mean(axis=0)
    lower = np.percentile(m, 2.5, axis = 0)
    upper = np.percentile(m, 97.5, axis = 0)
    
    return mean, lower, upper
def plot_results(mean, lower, upper):
   
    x = np.arange(mean.shape[0])
    plt.plot(x, mean)
    plt.errorbar(x, mean, yerr = (lower, upper))
    plt.show()

if __name__ == '__main__':
    """
        
    """
    n = int(10**3)
    array_ops  =  generateOperationArray(n)
    # aqui se crea un nodo del arbol 
    ABB = ABB()
    ABB.insert(0)
    m_time = sequence(node = ABB, sec = 100, n = n, subsample = 100, sequence_type='random')
    m, l, u = results(m_time)
    plot_results(m, l, u)



