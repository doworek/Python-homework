import os

dir = "C:\\Users\\User\\Documents\\STUDIA\\IV rok\\Python"

#changing words 'and', 'also', 'of' to 'AAA', 'BBB', 'CCC'
dict_words = {'and': 'AAA', 'also': 'BBB', 'of': 'CCC'}

for filename in os.listdir(dir):
	if filename.endswith('.txt'):
		#read input file
		file = open(filename, "r")
		data = file.read()
		for key in dict_words:
			data = data.replace(key, dict_words.get(key))
		file.close()
        #open the input file in write mode
		file = open(filename, "w")
        #overrite the input file with the resulting data
		file.write(data)
        #close the file
		file.close()