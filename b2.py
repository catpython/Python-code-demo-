

class Person(object):
	def __init__(self,first_name,last_name,father):
		self.first_name=first_name
		self.last_name=last_name
		self.father=father
	
	def printName(self):
		print("first_name:", self.first_name)
		print("last_name:", self.last_name)
		print("father:",self.first_name) #just for print as same as the father:4, father:5
		
	def getFather(self): 
		return self.father
#person_a = Person("User","1",None)
#person_b = Person("User","2",person_a)

person_a = Person("5","5",None)
person_b = Person("4","4",person_a)

a={
	"key1":1,
	"key2":{
		"key3":1,
		"key4":{
			"key5":4,
			"user":person_b,
		}
	}
}



def print_depth_extended(d, level=1):
	for (k,v) in d.items():
		print(k, level)
		if isinstance(v,dict):
			print_depth_extended(v,level+1)
		if isinstance(v,Person):
			v.printName()
			if v.getFather():
				fa= v.getFather()
				fa.printName()
			else:
				print("No father for this person")
print_depth_extended(a)


