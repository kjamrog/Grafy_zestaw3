#!/usr/bin/env python3.4


from sys import argv
from Graph import isGraphical
from Graph import Graph
from Dijkstra import dijkstra

	
seq = [int(i) for i in argv[1:]]
flag = isGraphical(seq)
if flag:
	graph = Graph(seq)
	graph.showAM()
	temp = graph.makeEV()
	dijkstra(graph)

