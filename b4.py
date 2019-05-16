import re

class Myclass:
	def isMatch(self, s: str, p: str)->bool:	
		print(s)
		"""
		if s.islower():
			#print("good s")
			pass
		else:
			print("s contained not lower case letter.")
				
		if p.islower():
			#print("good p")
			pass
		else:
			print("p contained not lower case letter.")
		"""
		
		print(p)
		p=p.replace("*", ".*")
		#print(p)		
		p=p.replace("?", ".?")
		
		p = "^"+p+"$"  #match should cover entire input string s
		#print(p)
		
		pattern = re.compile(p)
		match = pattern.match(s)
		
		
		if match:
			print("true")
			#print(match.group())
			return(True)
			
		else:
			print("false")
			return(False)

if __name__ == '__main__':				
	#s= "aa"
	#p= "*"

	#s= "cb"
	#p= "?a"

	s= "adceb"
	p= "*a*b"

	#s= "bcxb"
	#s= "bcba"
	#s= "bacb"
	#p= "b?b"
	#p= "*b?b"

	x= 	Myclass()	
	x.isMatch(s,p)

