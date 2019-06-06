import hashlib, sys 

# Args are "python hashget.py filename"
file = sys.argv
print("\033[1;31;40m \n")
print('1 - MD5 / 2 - SHA1')
menX = input()

if menX == 1: 
	def hash_file(filename): 
		h = hashlib.md5()
	
		with open (filename, 'rb') as file: 
		
			chunk = 0 
			while chunk != b'': 
				chunk = file.read(1024) 
				h.update(chunk)
			
		return h.hexdigest()

	message = hash_file(file[1])
	print (message)

if menX == 2: 
	def hash_file(filename): 
		h = hashlib.sha1()
	
		with open (filename, 'rb') as file: 
		
			chunk = 0 
			while chunk != b'': 
				chunk = file.read(1024) 
				h.update(chunk)
			
		return h.hexdigest()

	message = hash_file(file[1])
	print (message)