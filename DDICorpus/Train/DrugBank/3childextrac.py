#Extracting sentences with one or three child elements

# ONLY CONSIDERING, sentences with relationships among two entities.
# getchildren was deprecated

import xml.etree.ElementTree as ET
import re
import random
from os import path

with open("file.txt") as f1:
    text1 = f1.read()

filenames = re.split(r'[\n\r]+', text1)
filenames_trial = ["Abarelix_ddi.xml"]

for filename in filenames:
	print (filename)	
	tree = ET.parse(filename)
	root = tree.getroot()

	for sentence in root.findall('sentence'):
		#rank = sentence.find('pair')
		# print(list(sentence))
		if (len(list(sentence))!=3):
			root.remove(sentence)

	newfilepath = path.join('Edited_TEST',filename)
	print (newfilepath)
	tree.write(newfilepath)
