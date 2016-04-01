#!/usr/bin/env python3.4

from sys import maxsize
from Graph import Graph

# algorytm dijkstry

def dijkstra(graph, source):
	prevs={i:None for i in range(graph.vertex)}
	dist = {i:maxsize for i in range(graph.vertex)}
	dist[source] = 0
	S=[]
	Q=[i for i in range(graph.vertex)]
	while bool(Q):
		u = extractMin(Q,dist)
		S.append(u)
		for v in graph.AL[u]:
			if dist[v]>(dist[u]+graph.EV[u][v]):
				dist[v] = dist[u]+graph.EV[u][v]
				prevs[v] = u	
	return dist

def extractMin(Q, dist):
	i=Q[0]
	for v in Q:
		if dist[v]<dist[i]:
			i=v
	Q.remove(i)
	return i



# algorytm konstruujący macierz odległości między wierzchołakami

def distMatrix(graph):
	dijkstraLists = [dijkstra(graph, i) for i in range(graph.vertex)]
	matrix = [[dijkstraLists[i][j] for j in range(graph.vertex)] for i in range(graph.vertex)]

	return matrix
		

def centrum(matrix):
	l=sum(matrix[0])
	m=0
	for i in range(len(matrix)-1):
		s=sum(matrix[i+1])
		if s<l:
			l=s
			m=i+1
	print("Centrum tego grafu to wierzchołek ", m)

	
def minimax(matrix):
	l=max(matrix[0])
	m=0
	for i in range(len(matrix)-1):
		s=max(matrix[i+1])
		if s<l:
			l=s
			m=i+1
	print("Centrum mini-max tego grafu to wierzchołek ", m)











