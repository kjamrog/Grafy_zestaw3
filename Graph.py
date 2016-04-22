#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Moduł zawierający: 
# funkcję sprawdzającą czy ciąg jest graficzny
# klasę Graph

import networkx as nx
import matplotlib.pyplot as plt

from random import randrange

# sprawdzanie czy ciąg jest graficzny
def isGraphical(seq):
	length = len(seq)
	while True:
		seq.sort(reverse=True)
		x = seq[0]
		if x>=length:
			return False
		seq = seq[1:]
		seq = [seq[i]-1 if i < x else seq[i] for i in range(len(seq))]
		if not [i for i in seq if i !=0]:
			return True
		if seq[0] < 0:
			return False


# klasa Graph, tworzona na podstawie ciągu graficznego - zrobić dziedziczenie !
class Graph:
	# konstrukcja grafu
	def __init__(self, seq):
		self.seq = [i for i in seq]
		self.seq.sort(reverse=True)
		self.vertex = len(seq)
		#tworzenie kolejnych reprezentacji grafu, KOLEJNOŚĆ WYWOŁANIA WAŻNA !!!
		self.AM = self.makeAM()
		self.AL = self.makeAL()
		self.IM = self.makeIM()
		#edges values
		self.EV = self.makeEV()
		
				
	# wyświetlanie grafu				
	def showAM(self):
		for i in self.AM:
			print( [j for j in i])
	
	# tworzy macierz sąsiedztwa na podstawie ciągu graficznego
	def makeAM(self):
		seq = [i for i in self.seq]
		
		length = len(seq)
		AM = []
		AM = [[0 for i in range(length)] for vertices in seq]
		for vertice in range(length):
			
			next = vertice + 1
			while seq[vertice] > 0:
				while seq[next]==0:
					next+=1
				AM[vertice][next] = AM[next][vertice] = 1
				seq[vertice] -= 1	
				seq[next] -= 1
				next += 1
		return AM

		
	# tworzy listę sąsiedztwa
	def makeAL(self):
		length = len(self.AM)
		l=[[] for i in range(length)]
		for i in range(length):
			for j in range(length):
				if self.AM[i][j] == 1 :
					l[i].append(j)
		return l


	def makeIM(self):
		edges=self.countEdges()		
		vertices=len(self.AL)
		im=[[0 for i in range(vertices)] for j in range(edges)]
		n=0
		for i in range(len(self.AL)):
			for j in self.AL[i]:
				if j>i:
					im[n][i]=im[n][j]=1
					n=n+1		
		return im			
	
					
	def countEdges(self):
		n=0
		for i in range(len(self.AM)):
			for j in range(len(self.AM[i])):
				if self.AM[i][j]==1 and j>i:
					n=n+1
		return n


	def rand(self):
		from random import randrange
	
		edges=self.countEdges()
		edgesList=[[] for i in range(edges)]
		for i in range(len(self.IM)):
			for j in range(len(self.IM[i])):
				if self.IM[i][j]==1:
					edgesList[i].append(j)
		print(edgesList)			
	
		l, s = 0, 0
		while l<1:
			a=randrange(0,edges)
			b=randrange(0,edges)
			if a!=b:
				if (edgesList[a][0] not in edgesList[b]) and (edgesList[a][1] not in edgesList[b]):
					if [edgesList[a][0],edgesList[b][1]] not in edgesList and [edgesList[b][0],edgesList[a][1]] not in edgesList:					
						edgesList[a][1],edgesList[b][1]=edgesList[b][1],edgesList[a][1]
						l=l+1
			s=s+1
			if s>2000:
				print("Grafu nie można randomizować!")
				break
		# else:	
		# W tym miejscu po else dodać aktualizację wszystkich reprezentacji grafu!

		return edgesList
		
	def makeEV(self):
		from random import randint
		
		temp = [ [0 for j in i] for i in self.AM]
		for i in range(len(self.AM)):
			for j in range(i, len(self.AM)):
				if(self.AM[i][j] == 1):
					temp[i][j]=temp[j][i] = randint(1,9)
		return temp
		
	def draw(self):
		g = nx.Graph()
		for i in range(self.vertex):
			for j in range(i, self.vertex):
				if self.EV[i][j] != 0:
					g.add_edge(i, j, w=self.EV[i][j])
				
		pos = nx.shell_layout(g)
		nx.draw_networkx_nodes(g, pos, node_size=300)
		nx.draw_networkx_edges(g, pos)
		nx.draw_networkx_labels(g, pos)
		nx.draw_networkx_edge_labels(g, pos)

		plt.axis('off')
		plt.savefig("Graph.png")
		plt.close()
			

