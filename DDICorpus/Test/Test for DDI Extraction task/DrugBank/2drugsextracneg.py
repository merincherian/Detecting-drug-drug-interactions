#Seperating sentences with DDI(2drugs) into true DDIs

import xml.etree.ElementTree as ET
import re
import random
from os import path

with open("file.txt") as f1:
    text1 = f1.read()


filenames = re.split(r'[\n\r]+', text1)

for filename in filenames:	
	filepath = path.join('Edited2',filename)
	print (filepath)	
	tree = ET.parse(filepath)
	root = tree.getroot()



	idx = [] #list of indexes where true DDI is mentioned in pair tag
	cnt = 0 #find indexes where true DDI is found
	for sentence in root.iter('pair'):
		#print (sentence.attrib['ddi']	)
		if sentence.attrib['ddi']=="false":
			idx.append(cnt)

		cnt +=1

		

	print (idx)
	#print cnt


	cnt = 0
	cnt2 = 0 #index to acess list of indexes where true DDI sentences are there
	# Now remove sentences which are false and keep the remaining
	for sentence in root.findall('sentence'):
		
		if cnt2<len(idx):
			if cnt==idx[cnt2]:
				#print ("true")
				cnt2 += 1
			else:
				root.remove(sentence)	
		else:
			root.remove(sentence)

		cnt += 1 

	newfilepath = path.join('Negative',filename)
	print (newfilepath)
	tree.write(newfilepath)
