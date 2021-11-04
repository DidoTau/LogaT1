package com.company;

import org.jetbrains.annotations.NotNull;

public class Splay extends Node{
    private Node root;

    public Splay(){
        root = null;
    }

    int getHeight(Node node){
        return node == null ? -1:node.h;
    }
    void updateHeight(@NotNull Node node) {
        node.h = 1 + Math.max(getHeight(node.left), getHeight(node.right));
    }
     Node splay(Node node, int val)
    {
        // Base cases: root is null or
        // key is present at root
        if (node == null || node.val == val)
            return node;

        // Key lies in left subtree
        if (node.val > val)
        {
            // Key is not in tree, we are done
            if (node.left == null) return node;

            // Zig-Zig (Left Left)
            if (node.left.val > val)
            {
                // First recursively bring the
                // key as root of left-left
                node.left.left = splay(node.left.left, val);

                // Do first rotation for root,
                // second rotation is done after else
                node = rotateRight(node);
            }
            else if (node.left.val < val) // Zig-Zag (Left Right)
            {
                // First recursively bring
                // the key as root of left-right
                node.left.right = splay(node.left.right, val);

                // Do first rotation for root.left
                if (node.left.right != null)
                    node.left = rotateLeft(node.left);
            }

            // Do second rotation for root
            return (node.left == null) ?
                    node : rotateRight(node);
        }
        else // Key lies in right subtree
        {
            // Key is not in tree, we are done
            if (node.right == null) return node;

            // Zag-Zig (Right Left)
            if (node.right.val  > val)
            {
                // Bring the key as root of right-left
                node.right.left = splay(node.right.left, val);

                // Do first rotation for root.right
                if (node.right.left != null)
                    node.right = rotateRight(node.right);
            }
            else if (node.right.val < val)// Zag-Zag (Right Right)
            {
                // Bring the key as root of
                // right-right and do first rotation
                node.right.right = splay(node.right.right, val);
                node = rotateLeft(node);
            }

            // Do second rotation for root
            return (node.right == null) ?
                    node : rotateLeft(node);
        }
    }

    Node search(Node n, int val)
    {
        return splay(n,val);
    }



}
