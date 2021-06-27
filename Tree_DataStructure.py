'''
TREE:-
-------
Non-linear data structure
Represents relationship between nodes
Collection of entities is called nodes
Nodes are connected by edges

Characteristics of Tree :
-------------------------
1.Root Node
 Every tree has the root node
    ->top most node
    ->A tree can contain only one root node
2. in a tree if we have (N) nodes then we will have (N-1) edges/link
3.Every child will have only one parent but ------>parent can have multiple child

Degree of a node == No.s of children of the parent node.
degree of a tree == the highest degree

Height of a node
-----------------
the longest eges 


APPLICATION
--------------
Binary Search tree is use ti check the number present in the set or not(Search)

                                        Binary Tree
                                    -------------------

this tree have max 2 child node
-> it can have only 0,1,2 child
----------------------------------->>>>> there are 5 type of binary tree
                                            -->full binary tree
                                            -->complete binary tree
                                            -->perfect binary tree
                                            -->balanced binary tree
                                            -->pathological binary tree

Full binary tree
    Every node have 0,2 nodes
Complete Binary tree
    All levels (expect) last level 
                ->comletely filled with node
    last lavel 
                ->completely filled 
                -> left to right
Perfect binary tree 
    Type of binary tree in which all internal nodes contains 2 children and all 
    leaf node are in same level
Balanced Binary tree
    in which height of left and right subtree defer by one



    Binary search tree is a tree with following properties
------------------------------------------------------------------

1. The left subtree of a node contains only nodes with keys lesser than node"s key
2. The right subtree of a node contains only nodes with keys greater than node's key
3. The left subtree and rigt subtree each must also be a BST 
    
    Binary search tree (With duplicate values)
-------------------------------------------------------------------
some Books say 1.Duplicate values not allowed
some books say 2. if the node is equal to the root/node left <= root/node < rigt then the node will be in 
                  the left side tree
some books say 3. if the nodes is equal to the root/nodes left < root/node <= right then the node will be in 
                  the right sid of the tree    
'''

