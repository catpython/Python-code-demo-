


a={
	"key1":1,
	"key2":{
		"key3":1,
		"key4":{
			"key5":4
		}
	}
}

def print_depth(d, level=1):
	for (k,v) in d.items():
		print(k, level)
		if isinstance(v,dict):
			print_depth(v,level+1)

print('will print depth!, second commit')		
print_depth(a)
