# -*- coding: utf-8 -*-
# Moduł zawierający: 
# funkcję sprawdzającą czy ciąg jest graficzny
# klasę BaseGraph - bazowa klasa reprezentująca graf dla zestawów 2 i 3


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

	
# klasa Graph, tworzona na podstawie ciągu graficznego	
class BaseGraph:
	# konstrukcja grafu
	def __init__(self, seq):
		self.seq = [i for i in seq]
		self.seq.sort(reverse=True)
		self.vertex = len(seq)
		#tworzenie kolejnych reprezentacji grafu, KOLEJNOŚĆ WYWOŁANIA WAŻNA !!!
		self.AM = self.makeAM()
		self.AL = self.makeAL()
		self.IM = self.makeIM()
		
				
	# wyświetlanie grafu				
	def showAM(self):
		print( "\nMacierz sąsiedztwa:\n" )
		for i in self.AM:
			print( [j for j in i])
	
	def showAL(self):
		print( "\nLista sąsiedztwa:\n" )
		for i in range(len(self.AL)):
			print(str(i)+" -> "+str(self.AL[i]))
			
	def showIM(self):
		print( "\nMacierz incydencji:\n")
		for i in self.IM:
			print( [j for j in i])
	
	# tworzy macierz sąsiedztwa na podstawie ciągu graficznego
	def makeAM(self):
		seq = [i for i in self.seq]
		#pomocnicza lista dwuelementowych list (pierwszy element każdej listy to wartość a drugi to indeks tej wartosci w seq)
		pom = [[seq[i],i] for i in range(len(seq))]
		length = len(seq)
		AM = []
		AM = [[0 for i in range(length)] for vertices in seq]
		for s in range(length):
			pom.sort(reverse=True, key=lambda x:x[0])
			vertice = 0
			next = vertice + 1
			while pom[vertice][0] > 0:
				while pom[next][0]==0:
					next+=1
				AM[pom[vertice][1]][pom[next][1]] = AM[pom[next][1]][pom[vertice][1]] = 1
				pom[vertice][0] -= 1	
				pom[next][0] -= 1
				seq[pom[vertice][1]] -=1
				seq[pom[next][1]] -=1
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

		l, s = 0, 0
		a, b = None, None
		# wyszukiwanie i zamiana krawędzi
		while l<1:
			a=randrange(0,edges)
			b=randrange(0,edges)
			if a!=b:
				if (edgesList[a][0] not in edgesList[b]) and (edgesList[a][1] not in edgesList[b]):
					if [edgesList[a][0],edgesList[b][1]] not in edgesList and [edgesList[b][0],edgesList[a][1]] not in edgesList and [edgesList[b][1],edgesList[a][0]] not in edgesList and [edgesList[a][1],edgesList[b][0]] not in edgesList:					
						edgesList[a][1],edgesList[b][1]=edgesList[b][1],edgesList[a][1]
						l=l+1
			s=s+1
			if s>2000:
				print("Grafu nie można randomizować!")
				return
		# aktualizacja reprezentacji grafu
		w, x, y, z = edgesList[a][0], edgesList[b][1], edgesList[b][0], edgesList[a][1]
		self.AM[w][x]=self.AM[x][w]=self.AM[y][z]=self.AM[z][y]=0
		self.AM[w][z]=self.AM[z][w]=self.AM[y][x]=self.AM[x][y]=1
		self.AL = self.makeAL()
		self.IM = self.makeIM()

	# rosowanie grafu
	def draw(self):
		pass
