class Node():
	def __init__(self,value,parent):
		self.value=value
		self.parent=parent
		self.ancestor = []		
	
	def add_ancestor(self,node):
		self.ancestor.append(node)
		
	def __iter__(self):
		return iter(self.ancestor)
		
	def list_ancestor(self):
		yield self
		for c in self:
			yield from c.list_ancestor()
	
		
n1 = Node(1,1)	
n2 = Node(2,1)	
n3 = Node(3,1)	
n4 = Node(4,2)	
n5 = Node(5,2)	
n6 = Node(6,3)	
n7 = Node(7,3)	
n8 = Node(8,4)	
n9 = Node(9,4)	

nlist = [n1,n2,n3,n4,n5,n6,n7,n8,n9]

n9.add_ancestor(n4)
n8.add_ancestor(n4)
n7.add_ancestor(n3)
n6.add_ancestor(n3)
n5.add_ancestor(n2)
n4.add_ancestor(n2)
n3.add_ancestor(n1)
n2.add_ancestor(n1)


def lca(node1,node2):	
	cm = (ch1 for ch1 in node1.list_ancestor() for ch2 in node2.list_ancestor() if ch1.value== ch2.value)
	print("least common ancestor for node: " , node1.value, " and node: ", node2.value, " is:")
	print(next(cm).value)
	#print(next(cm).value)
	print()


		
lca(n6, n7)
lca(n3, n7)
lca(n3,n3)
lca(n9, n2)
lca(n9, n5)
lca(n9, n8)

#Two generators are used to avoid big memory consuming.
#may use tracemalloc to check the memory