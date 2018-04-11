# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 13:18:29 2018

@author: jeppe
"""
import networkx as nx
#import math
import sys
import time as tm

time0=tm.time()
with open(sys.argv[1], "rb") as infile:
    next(infile)
    G=nx.read_adjlist(infile, create_using=nx.DiGraph(),nodetype=int)
    GS = nx.stochastic_graph(G,copy=True)
    no_nodes = GS.number_of_nodes()
    m = 0.15#dampening factor
    nodes = G.nodes()
    edges = G.edges()
    degree_dict = {}#keeps in_degree of all nodes
    dangling_dict = {}
    page_rank = {}#dict to return rank of nodes
    visit_dict = {}#dict to keep track of nr. of visits for each node
    for node in nodes:#Enter nodes and their in_degrees to degree_dict (if they aren't dangling)
        if G.in_degree(node) != 0:
            degree_dict[node]=G.in_degree(node)/no_nodes
        else:
            dangling_dict[node]=m
    print(degree_dict)
#    print(tm.time()-time0)
#    page_list = [[0]*no_nodes]*no_nodes
