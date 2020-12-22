import os

dir = "C:\\Users\\User\\Documents\\STUDIA\\IV rok\\Python"

#deleting 'and'

for filename in os.listdir(dir):
	if filename.endswith('.txt'): 
		#read input file
		file = open(filename, "r")
		data = file.read()
		data = data.replace('and', '')
		file.close()
		#open the input file in write mode
		file = open(filename, "w")
		#overrite the input file with the resulting data
		file.write(data)
		file.close()