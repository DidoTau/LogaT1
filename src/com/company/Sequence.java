package com.company;
import java.util.Random;

public class Sequence {
    private int n;
    private int [] arrayOps;
    public Sequence(int n){
        this.n = n;
        this.arrayOps = generateOperationArray(n);
    }
    /**
    Genera una operacion al azar
    * */
    int generateOperation(){
        Random rand = new Random();
        int random_int = rand.nextInt(100);
        if( 0<random_int && random_int<50){
            return 0; // insertar
        }
        else if(50<random_int && random_int<83){
            return 1; // búsqueda wena
        }
        else{
            return 2; // búsqueda mala
        }
    }
    /**
     Genera un millon de operaciones
     * */
    int [] generateOperationArray(int ops){
        int [] ops_array = new int[ops]; // 10^6 de operaciones
        for ( int i = 0; i < ops;i++){
            ops_array[i] = generateOperation();
        }
        return ops_array;
    }
    void operator(Node node, int val, int op){
        if(op == 0){ // insercion
            node.insert(val);
        }
        else if(op ==1){ // busqueda wena
            node.search(val);
        }
        else { //busqueda mala
            node.search(val);
        }
    }
    void random(Node node, int op, int [] arr){
        Random rand = new Random();
        int random_int = rand.nextInt(1000000);
        if(op == 0 || op == 2){ // insercion or busqueda mala
            while(arr[random_int]==1){ // mientras está en el arreglo
                random_int = rand.nextInt(1000000); // genero otro
            }
            operator(node, random_int, op);
        }
        else if(op ==1){ // busqueda wena
            while(arr[random_int]==0){ // mientras no está en el arreglo
                random_int = rand.nextInt(1000000); // genero otro hasta encontrar uno que si esté
            }
            operator(node, random_int, op);
        }

    }

    float [] sequence(Node tree, int sec){

        float [] times = new float[1000]; // 1000 tiempos
        for ( int i = 0; i < sec;i++){
            int [] arr_values = new int[this.n]; // 10^6 de valores
            for (int j = 0; j<this.n; j++){
                int op = this.arrayOps[j]; // operacion a realizar
                random(tree, op, arr_values);
            }
        }
        return times;
    }
}
