"""

"""


import copy
import sys
import os.path
import numpy as np
from functions import clear
from tree import Tree
from functions import private_from, list_gate_comb


"""

"""
def split_sub_tree_or(tree, id):
    split_or = []

    if tree.node_exists(id):
        node = tree.get_node(id)
        gate = node.get_gate()
        children = node.get_children()

        if "/" in gate:
            node.set_gate("AND")

            (str_k, str_n) = gate.split("/")
            k = int(str_k)

            tmp_children = copy.deepcopy(children)

            lgc = list_gate_comb(tmp_children, k)

            for i in range(len(lgc)):
                diff_list = private_from(tmp_children, lgc[i])
                lgc[i] = diff_list

            for list in lgc:
                tmp_tree = copy.deepcopy(tree)

                for id_child in list:
                    node_child = tmp_tree.get_node(id_child)
                    tmp_tree.delete_sub_tree_from_node(node_child)

                split_or.append(tmp_tree)
        else:
            tmp_children = copy.deepcopy(children)

            for id_child in tmp_children:
                tmp_tree = copy.deepcopy(tree)

                for tmp_id_child in tmp_children:
                    if tmp_id_child != id_child:
                        node_child = tmp_tree.get_node(tmp_id_child)
                        tmp_tree.delete_sub_tree_from_node(node_child)

                split_or.append(tmp_tree)

    return split_or

"""

"""
def pathway_tree(tree):
    nodes = tree.get_nodes()
    id_nodes_sub_tree_or = []

    for node in nodes:
        gate = node.get_gate()

        if not (node.is_leaf()) and gate != "AND":
            id = node.get_id()
            id_nodes_sub_tree_or.append(id)

    list_tree = [tree]

    for id_node in id_nodes_sub_tree_or:
        tmp = copy.deepcopy(list_tree)

        for tmp_tree in tmp:
            if tmp_tree.node_exists(id_node):
                list_split_tree = split_sub_tree_or(tmp_tree, id_node)

                list_tree += list_split_tree
                list_tree.pop(0)

    return list_tree

"""

"""
def paths_tree(tree):
    pathway = pathway_tree(tree)
    list_paths = []

    for pw in pathway:
        root = pw.get_root()
        paths = pw.find_path(root)

        list_paths.append(paths)

    return list_paths

def print_t(tree):
    nodes = tree.get_nodes()

    for node in nodes:
        id = node.get_id()
        print(id)


"""

"""

clear()

t = Tree()

name_file = input("Enter the JSON file name: ")

if not (os.path.isfile(name_file)):
    print("\nError \"test_tree.py\"")
    print("The file '", name_file, "' does not exist", sep="")

    sys.exit()

t.from_json_to_tree(name_file)

clear()

list_tree = pathway_tree(t)

for path in list_tree:
    root = path.get_root()
    print(path.find_path(root))
