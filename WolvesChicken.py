import numpy as np

startfile = np.loadtxt("start1.txt", delimiter=",")
goalfile = np.loadtxt("goal1.txt", delimiter=",")
leftbank=startfile[0]
rightbank=startfile[1]
leftnumchick=leftbank[0]
rightnumchick=rightbank[0]
leftboatstate=leftbank[2]
rightnumwolv=rightbank[1]
leftnumwolv=leftbank[1]
rightboatstate=rightbank[2]
goalleftbank=goalfile[0]
goalrightbank=goalfile[1]
goalleftnumchick=goalleftbank[0]
goalrightnumchick=goalrightbank[0]
goalleftboatstate=goalleftbank[2]
goalrightnumwolv=goalrightbank[1]
goalleftnumwolv=goalleftbank[1]
goalrightboatstate=goalrightbank[2]
startstate=[leftnumchick,leftnumwolv,leftboatstate,rightnumchick,rightnumwolv,rightboatstate]
print(startstate)
goalstate=[goalleftnumchick,goalleftnumwolv,goalleftboatstate,goalrightnumchick,goalrightnumwolv,goalrightboatstate]
print(goalstate)
#bfs 
def expand(node,problem):
	print("Exapanding")
	successors=[]
	for i in range(20):
		s=[]
		parent=node
		state[i]=result
	
def bfs(state):
	print("BFS")



def dfs(state):
	print("DFS")


def iddfs(state):
	print("iddfs")


def astar(state):
	print("Astar")

def expand():
	print("Exapanding")
	


	

if __name__=="__main__":
	print("Implementation")


