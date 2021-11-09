import numpy as np 
import time
import matplotlib.pyplot as plt
import sys
import math 

from ABB import *
from AVL import *
from Splay import *
from Btree import *

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
        in_index = np.where(arr == 0)[0] # indices de valores no existentes
        random_int = np.random.choice(in_index)
        operator(node, random_int, op, arr)
    elif op ==1:                                     #si es busqueda buena
        in_index = np.where(arr == 1)[0] # indices de valores existentes 
        random_int = np.random.choice(in_index)
        operator(node, random_int, op, arr)

def increasing(node,op, arr, n, k):
    """
    Genera numeros que tienden a ser creciente para insertar pero q onda con los otros???????

    Args:
        node ([type]): [description]
        op ([type]): [description]
        arr ([type]): [description]
        n ([type]): [description]
    """
    random_int = np.random.randint(low = 0, high = k)    
    if op == 0: # si insertamos
        m = np.sum(arr)
        random_int+= m #le agregamos la cantidad de agregados
        operator(node, random_int, op, arr) #op insertar

    elif op == 2: #busqueda mala
        while arr[random_int] == 1: # mientras este en el arreglo
            random_int = np.random.randint(low = 0, high = k)       #generamos otro
        operator(node, random_int, op, arr)   

    else: # op ==1:                                     #si es busqueda buena
        in_index = np.where(arr == 1) # indices de valores existentes 
        random_int = np.random.choice(in_index)
        operator(node, random_int, op, arr)

def biased(node, op, arr, n, arr_prob,f):
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
    
    if op == 0 : #insertar
        random_int = np.random.randint(low = 0, high = n)     # si insercion o busqueda mala
        while arr[random_int] != 0:                  # mientras este en el arreglo
            random_int = np.random.randint(low = 0, high = n)       # generamos otro
        operator(node, random_int, op, arr)
        arr_prob[random_int] = f(random_int)/arr_prob.sum()  # ACTUALIZAR P !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif op ==1:
        random_int = np.random.choice(np.arange(n), arr_prob)     # si es busqueda buena
        while arr[random_int] == 0:                   # mientras no est en el arreglo
            random_int =  np.random.randint(low = 0, high = n)   # generamos otro
        operator(node, random_int, op, arr)
    else: # busqueda mala op = 2    
        while arr[random_int] == 1:      #mientras esté en el arreglo
            random_int = np.random.randint(low = 0, high = n)     #generamos otro
        operator(node, random_int, op, arr)            

def sequence(node, sec, n, subsample, sequence_type ,k = 0, f = None):
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
            if i != 0:
                node.reset()
                node.insert(0)
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
            if i!= 0: 
                node.reset()
                node.insert(0) 
             
            arr_values = np.zeros(n)
            arr_values[0] = 1 # 0 existe
            times_i = []  # tiempos por sec
            start_time = time.process_time() 
            for j in range(n):               #recorremos el arreglo de operaciones?
                op = array_ops[j]   
                increasing(node, op, arr_values,k)
                if (j+1)  %subsample == 0 and j !=0: # cada mil ca
                    times_i.append(time.process_time()- start_time)
            times.append(times_i)  #agregamos arr tiempos por         
    elif sequence_type == "biased":
        for i in range(sec): #100 
            if i!= 0 : 
                node.reset()
                node.insert(0) 
            arr_prob = np.zeros(n)   
            arr_values = np.zeros(n)
            arr_values[0] = 1 # 0 existe
            arr_prob[0] = f(0)
            times_i = []  # tiempos por sec
            start_time = time.process_time() 
            for j in range(n):               #recorremos el arreglo de operaciones?
                op = array_ops[j]   
                biased(node, op, arr_values, arr_prob)
                if (j+1)  %subsample == 0 and j !=0: 
                    times_i.append(time.process_time()- start_time)
            times.append(times_i)  #agregamos arr tiempos por        
    return times

def results(m, save = False):
    """[summary]

    Args:
        m ([type]): [description]

    Returns:
        [type]: [description]
    """
    m = np.array(m)
    mean =  m.mean(axis=0)
    std = m.std(axis = 0)
    lower = mean -  std/ math.sqrt(m.shape[0])
    upper =  mean +  std/ math.sqrt(m.shape[0])
    return mean, lower, upper
def plot_results(mean, lower, upper):
   
    x = np.arange(mean.shape[0])
    plt.plot(x, mean)
    plt.errorbar(x, mean, yerr = (lower, upper))
    plt.show()
def string_to_function(name):
    if name == 'id':
        return lambda x: x
    elif name =='sqrt':
        return lambda x: x**0.5
    elif name == 'ln':
        return lambda x: math.log(x)

if __name__ == '__main__':
    """
        
    """
    tree = sys.argv[1]
    seq = sys.argv[2]
    n = int(10**5)
    sec = 100 # experimentos
    subsample = 100 # subsampleo
    array_ops  =  generateOperationArray(n)
    # aqui se crea un nodo del arbol 
    if tree == 'ABB':
        ABB = ABB()
        ABB.insert(0)
         # ABB RANDOM
        if seq == 'random':
            m_time = sequence(node = ABB, sec = sec, n = n, subsample = subsample, sequence_type='random')
        if seq == 'increasing':
            pass
        if seq == 'biased':
            arg = sys.argv[3]
            m_time = sequence(node = ABB, sec = sec, n = n, subsample = subsample, sequence_type='random', f = string_to_function(arg))


    if tree == 'AVL':
        AVL = AVL()
        AVL.insert(0)
        if seq == "random":
            m_time = sequence(node = AVL, sec = sec, n = n, subsample = subsample, sequence_type='random')
        if seq == 'biased':
            arg = sys.argv[3]
            m_time = sequence(node = AVL, sec = sec, n = n, subsample = subsample, sequence_type='random', f = string_to_function(arg))

    if tree == 'Splay':
        Splay =  Splay()
        Splay.insert(0)
        if seq == "random":
            m_time = sequence(node = Splay, sec = sec, n = n, subsample = subsample, sequence_type='random')
        if seq == 'biased':
            arg = sys.argv[3]
            m_time = sequence(node = Splay, sec = sec, n = n, subsample = subsample, sequence_type='random', f = string_to_function(arg))
    if tree == 'Btree':
        B = int(sys.argv[4])
        Btree = Btree(B)
        Btree.insert(0)
        if seq == "random":
            m_time = sequence(node = Btree , sec = sec, n = n, subsample = subsample, sequence_type='random')
        if seq == 'biased':
            arg = sys.argv[3]
            m_time = sequence(node = Btree , sec = sec, n = n, subsample = subsample, sequence_type='random', f = string_to_function(arg))
    
    m, l, u = results(m_time)
    np.save('../experimentos/{}/{}_{}_mean.npy'.format(tree,tree, seq), m)
    np.save('../experimentos/{}/{}_{}_lower.npy'.format(tree,tree, seq), l)
    np.save('../experimentos/{}/{}_{}_upper.npy'.format(tree,tree, seq), u)
    plot_results(m, l, u)
