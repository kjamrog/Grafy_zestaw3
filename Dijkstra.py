#!/usr/bin/env python3.4

from sys import maxint
from Graph import Graph

# algorytm dijkstry
# argument macierz odległości między wierzchołkami

def dijkstra(graph, source):
	
	vset = []
	dist = []
	dist.append(0, None)
	
	for v in range(graph.vertex-1):
		dist.append( (maxint, None) )
		vset.appand(v+1)
		
	
		
	
