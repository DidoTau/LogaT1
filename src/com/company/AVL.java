package com.company;

import org.jetbrains.annotations.NotNull;

public class AVL extends Node{
    private Node root;

    public AVL(){
        root = null;
    }

    int getBalance(Node node){
        return (node == null) ? 0 : getHeight(node.right)- getHeight(node.left);
    }

    Node insert(Node node, int val){
        return balance(this.insert(val));
    }

    Node balance(Node node){
        updateHeight(node);
        int balance = getBalance(node);
        if(balance > 1){
            if (getHeight(node.right.right) > getHeight(node.right.left)){
                node = rotateLeft(node);
            }
            else {
                node.right = rotateRight(node.right);
                node = rotateLeft(node);
            }
        }
        else if (balance < -1){
            if(getHeight(node.left.left) > getHeight(node.left.right)){
                node = rotateRight(node);
            }
            else {
                node.left = rotateLeft(node.left);
                node = rotateRight(node);

            }
        }
        return node;
    }

    Node search(int val){
        Node current = root;
        while(current!=null){
            if(current.val == val){
                break;
            }
            current = current.val < val ? current.right : current.left;
        }
        return current;
    }
}
