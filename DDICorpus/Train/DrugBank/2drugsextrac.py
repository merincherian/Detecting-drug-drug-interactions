#Extracting sentences which only describe DDI(2 drugs)

import xml.etree.ElementTree as ET
import re
import random
from os import path

with open("file.txt") as f1:
    text1 = f1.read()


filenames = re.split(r'[\n\r]+', text1)

for filename in filenames:	
	filepath = path.join('Edited',filename)	
	print (filepath)	
	tree = ET.parse(filepath)
	root = tree.getroot()


	for sentence in root.findall('sentence'):
		rank = sentence.find('pair')
		print (rank)        
		if rank is  None:
			root.remove(sentence)	
	
	newfilepath = path.join('Edited2',filename)
	print (newfilepath)
	tree.write(newfilepath)
