#!/usr/bin/env python3.4

from sys import maxsize
from Graph import Graph

# algorytm dijkstry, jako argument przyjmuje graf oraz nr wierzchołka stanowiącego źródło
# zwraca słownik, w którym kluczem są wierzchołḱi a wartościami ich odległości od źródła
# wypisuje ścieżki pomiędzy danym wierzchołkiem a źródłem

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
	
	print("\nScieżki pomiędzy poszczególnymi wierzchołkami dla źródła",source,":")
	for i in range(graph.vertex):
		if(i==source):
			continue
		w=i
		print("from",i , "to", source, end=":\n")
		while prevs[w]!=None:
			w=prevs[w]
			print("->",w, end=" ")
		print()


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
		

# algorytm wypisujący centrum grafu

def centrum(matrix):
	l=sum(matrix[0])
	m=0
	for i in range(len(matrix)-1):
		s=sum(matrix[i+1])
		if s<l:
			l=s
			m=i+1
	print("Centrum tego grafu to wierzchołek ", m)


# algorytm wypisujący centrum mini-max grafu
	
def minimax(matrix):
	l=max(matrix[0])
	m=0
	for i in range(len(matrix)-1):
		s=max(matrix[i+1])
		if s<l:
			l=s
			m=i+1
	print("Centrum mini-max tego grafu to wierzchołek ", m)




# algorytm prima
class PriorityQueue:
	def __init__(self, vertex):
		self.d = {i:20 for i in range(vertex)}
		
		
	def pop(self):
		minimum = min(self.d.values())
		u=0
		for i in self.d:
			if self.d[i]==minimum:
				u=i
				break
		self.d.pop(u)
		return u
		
	def empty(self):
		return self.d
		
	
def prim(graph, r):
	q = PriorityQueue(graph.vertex)
	q.d[r] = 1

	pre = [None for i in range(graph.vertex)]
	
	while q.empty():
		u = q.pop()
		for v in graph.AL[u]:
			if v in q.d and graph.EV[u][v] < q.d[v]:
				pre[v] = u
				q.d[v] = graph.EV[u][v]
	return pre

