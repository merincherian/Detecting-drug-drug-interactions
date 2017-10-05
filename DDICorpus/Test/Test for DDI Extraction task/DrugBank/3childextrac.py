#Extracting sentences with one or three child elements

import xml.etree.ElementTree as ET
import re
import random
from os import path

with open("file.txt") as f1:
    text1 = f1.read()


filenames = re.split(r'[\n\r]+', text1)

for filename in filenames:
	print (filename)	
	tree = ET.parse(filename)
	root = tree.getroot()


	for sentence in root.findall('sentence'):
		rank = sentence.find('pair')
		if (len(sentence.getchildren())!=3) and (len(sentence.getchildren())!=1):
			root.remove(sentence)

	newfilepath = path.join('Edited',filename)
	print (newfilepath)
	tree.write(newfilepath)
