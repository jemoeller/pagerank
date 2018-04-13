# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 13:18:29 2018

@author: jeppe
"""
import networkx as nx
import sys
import time as tm
from collections import Counter

# =============================================================================
# Pagerank using dictonaries
# =============================================================================
def page_rank(graph):
    graph_out = nx.stochastic_graph(graph,copy=True)#graph where out-edges of each node has a sum of 1 
    no_nodes = graph_out.number_of_nodes()#nodes in graph
    damp = 0.15#dampening factor
    rank_dict = dict.fromkeys(graph_out, 1.0 / no_nodes)#contains nodes and their rank. Initially importance is uniformally distributed among nodes 
    p = dict.fromkeys(graph_out, 1.0 / no_nodes)#
    dangling_weight_dict = p#
    dangling_nodes = [node for node in graph_out if graph_out.out_degree(node,weight="weight") == 0.0]#contains nodes with no initial weight
    check = True
#    print(dangling_nodes)
    while check == True:
        rank_dict_copy = rank_dict
        rank_dict = dict.fromkeys(rank_dict_copy.keys(), 0)
        dangle_sum = damp * sum(rank_dict_copy[node] for node in dangling_nodes)
        for node in rank_dict:
            for n in graph_out[node]:
                rank_dict[n] += damp * graph_out[node][n]["weight"] * rank_dict_copy[node]
            rank_dict[node] += dangle_sum * dangling_weight_dict[node] + p[node] * (1.0 - damp)#x_{k+1} = (1 − m)Axk + (1 − m)Dxk + mSxk
        if rank_dict_copy == rank_dict: #if there is no change after computations returns rank_dict
            check = False#stops loop
            return rank_dict


if __name__ == "__main__":
    time0=tm.time()
    with open(sys.argv[1], "rb") as infile:
        next(infile)
        G=nx.read_adjlist(infile, create_using=nx.DiGraph(),nodetype=int)#directed graph
        rank = page_rank(G)
        count = Counter(rank)
        num = 1
        print("\n")
        print("The ranking of each node is as follows:","\n")
        for k,v in count.most_common(10):
            if num < 10:
                print("({}) |node nr.{}| rank: {}".format(num,k,v),"\n")
            num += 1
#        print("==================================================","\n")
#        for k,v in rank.items():
#            print("node {}, rank: {}".format(k,v),"\n")
#         print("==================================================","\n")
    print("Calculations took {} seconds.".format(tm.time()-time0))
        