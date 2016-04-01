#!/usr/bin/env python3.4


from sys import argv
from sys import maxsize
from Graph import isGraphical
from Graph import Graph
from Dijkstra import dijkstra
from Dijkstra import distMatrix
from Dijkstra import centrum
from Dijkstra import minimax
	
seq = [int(i) for i in argv[1:]]
flag = isGraphical(seq)
if flag:
	graph = Graph(seq)
	print("Macierz sąsiedztwa:")
	graph.showAM()
	print("\nMacierz wag poszczególnych krawędzi:")
	for i in range(len(graph.EV)):
		print(graph.EV[i])
	

	dists= distMatrix(graph)
	print("\nMacierz odległości wierzchołków:")
	for i in dists:
		print(i)
	print()

	centrum(dists)
	minimax(dists)

