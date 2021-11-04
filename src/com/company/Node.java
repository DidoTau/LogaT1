package com.company;
import org.jetbrains.annotations.NotNull;

import java.util.Scanner;

public class Node {
    int val;
    int h;
    Node left;
    Node right;
    Node parent;

    public Node(){
       left = null; right = null; parent = null;
       val = 0;
       h = 0;
    }
    public Node(int val){
        left = null; right = null;
        this.val = val;
        h = 0;
    }
    Node insert(Node node, int val){
        // llega a un nodo vacío, crea el nodo con el valor ingresado
        if(node==null){
            return new Node(val);
        }
        // insertar a la izquierda si es menor que el valor del nodo actual
        else if(val < node.val){
            node.left = insert(node.left, val);
        }
        // insertar a la derecha si es mayor que el valor del nodo actual
        else if (val > node.val){
            node.right = insert(node.right, val);
        }
        else {
            throw new RuntimeException("valor duplicado!");
        }
        return node;
    }
    int getHeight(Node node){
        return node == null ? -1:node.h;
    }
    void updateHeight(@NotNull Node node) {
        node.h = 1 + Math.max(getHeight(node.left), getHeight(node.right));
    }
    Node rotateLeft(Node node) {
        Node r = node.right;
        Node rl = r.left;
        r.left = node;
        node.right = rl;
        updateHeight(node);
        updateHeight(r);
        return r;
    }

    Node rotateRight(Node node) {
        Node l = node.left;
        Node lr = l.right;
        l.right = node;
        node.left = lr;
        updateHeight(node);
        updateHeight(l);
        return l;
    }
}
