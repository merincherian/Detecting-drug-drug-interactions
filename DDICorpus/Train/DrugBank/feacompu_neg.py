# Compute the 9 features

from nltk.tokenize import word_tokenize
import xml.etree.ElementTree as ET
from nltk.corpus import stopwords
import string
import re
from nltk import *
import csv
from os import path

#with open('ML/trainFeatures1.csv', 'a') as f:
#        w = csv.writer(f, delimiter = ',')
#        w.writerow(['F1', 'F2', 'F3','F4','F5','F6','F7','F8','F9','Class'])

with open("file.txt") as f1:
    text1 = f1.read()


filenames = re.split(r'[\n\r]+', text1)

for filename in filenames:	
	filepath = path.join('Negative',filename)
	print (filepath)
	
	tree = ET.parse(filepath)
	root = tree.getroot()


	stop_words = set(stopwords.words("english"))  # load stopwords

	#Extract from xml file the stemmed sentences
	sentences = []
	cleaned_text_final = []
	text_final = []
	for sentence in root.findall('sentence'):
		text=sentence.get('text')
		text_final.append(text)
		text = text.lower()
		#print (text)
		example_words = word_tokenize(text)
		# removing punctuations
		example_words = list(filter(lambda x: x not in string.punctuation, example_words))
		# removing stopwords 
		cleaned_text = list(filter(lambda x: x not in stop_words, example_words))
		cleaned_text_final.append(cleaned_text)
		#print(cleaned_text)
		ps = PorterStemmer()
		stem=list(map(lambda x: ps.stem(x), cleaned_text))
		#print (stem)
		sentences.append(stem)
		'''lemmatizer = WordNetLemmatizer()
		lem=list(map(lambda x: lemmatizer.lemmatize(x), stem))
		print (lem)
	    '''    

	if not cleaned_text_final:
		print ("I knew it")

	else:
		
		drugs_pairs = []
		temp1 = []
		temp2 = []
		temp3 = []
		count = 0
		for entity in root.iter('entity'):
		     text=entity.get('text')
		     #print (text.lower())
		     count += 1
		     if count%2==0:    
		     	temp2.append(text.lower())
		     #newtext=text.lower()
		     else:
		     	temp1.append(text.lower())	
		    
		     
		size=len(temp1)

		for i in range(size):
			temp3.append(temp1[i])
			temp3.append(temp2[i])
			drugs_pairs.append(temp3)
			temp3 = []

		#print (len(drugs_pairs[0]))

		#Splitting drug names with space in between into two
		#print (drugs_pairs)
		'''
		final_drugs_pairs = []
		for drugs in drugs_pairs:
			#print (drugs)
			if len(drugs)>1:
				#print ("check")
				for drug in drugs:
					#print (drug)
					words = drug.split(" ")
					#print (words[0])

			#tokenized_drug = word_tokenize(drug)
			#print (tokenized_drug)
		'''

		#************************************ Stores words into a variable from text files ****************************************************

		with open("positive.txt") as f1:
		    text1 = f1.read()
		#Stemming
		positive = re.split(r'[\n\r]+', text1)
		#print ("positive",positive)
		ps = PorterStemmer()
		positives = list(map(lambda x: ps.stem(x), positive))
		#print ("positivves",positives)

		with open("negative.txt") as f1:
			text1 = f1.read()
		#Stemming
		negative = re.split(r'[\n\r]+', text1)
		ps = PorterStemmer()
		negatives = list(map(lambda x: ps.stem(x), negative))


		with open("special.txt") as f1:
		    text1 = f1.read()

		specials = re.split(r'[\n\r]+', text1)
		#Stemming
		special = re.split(r'[\n\r]+', text1)
		ps = PorterStemmer()
		specials = list(map(lambda x: ps.stem(x), special))


		#************************************ Computing the features ****************************************************

		DDI_scope = 3
		
		idx_drugs = -1 #index for the drug_pairs list
		i = 0
		for sentence in sentences:
			#print (sentence,drugs_pairs[idx_drugs])
			#print("hello all:",sentence)
			print ("sentence:",sentence)
			cnt = 0
			idx_drugs += 1 #index for the drug_pairs list
			print ("idx_drugs:",idx_drugs)
			idx1 = -1 #index for drug 1
			idx2 = -1 #index for drug 2
			#-> flags is list of values that tell
			#   whether the drug name has a space in between
			#   or not and this is important to know for feature calculation
			flags = []
			for drug in drugs_pairs[idx_drugs]:
				drug_split = drug.split(" ")
				if len(drug_split)>1:
					flags.append(1)
				else:
					flags.append(0)

			for word in cleaned_text_final[i]:
				#print (word)
				if idx_drugs > 1: #we don't want to check for more than two drugs
					print ("helo")	
					break
				for drug in drugs_pairs[idx_drugs]:
					#print (drug)
					drug_split = drug.split(" ")
					#print (word,drug_split[0])
					if word==drug_split[0] and idx1==-1:
						if flags[0]==1:
							idx1 = cnt + 1
						else:
							idx1 = cnt
						#idx_drugs += 1
						continue

					elif word==drug_split[0] and idx2==-1:
						if flags[1]==1:
							idx2 = cnt + 1
						else:
							idx2 = cnt
						#idx_drugs += 1
						continue
					
					if idx_drugs > 1: #we don't want to check for more than two drugs
						print ("helo")	
						break	
					
				cnt +=1

			print ("indexes:",idx1,idx2)
			print ("flags",flags)
			i += 1

			#-> Compute first feature i.e number of positive 
			#   keywords in whole sentence
			cnt = 0 #count number of positive keywords
			print (sentence)
			for word in sentence:
				print (word)
				for positive in positives:
					if positive=="decreas":
						print ("rishi")
					if word==positive:
						cnt += 1
						break

			feature1 = cnt
			print ("feature1:",feature1)

			#-> Compute second feature i.e whether one or more positive 
			#   exist between the two drug names

			cnt = 0
			feature2 = 0 #check whether feature 2 is true or not
			for word in sentence[idx1+1:idx2]:
				for positive in positives:
					if word==positive:
						cnt += 1
						break

			if cnt>=1:
				feature2 = 1
			print ("Feature2:",feature2)

			#-> Compute third feature i.e whether one or more positive 
			#   exist within scope but not between the two drug names

			cnt = 0
			feature3 = 0 #check whether feature 3 is true or not
			#Check before first drug name
			if ( (idx1+1) > DDI_scope):
				for word in sentence[(idx1-DDI_scope):idx1]:
					for positive in positives:
						if word==positive:
							cnt += 1
							break

			#Check after second drug name
			if ( (len(sentence)-(idx2+1)) > DDI_scope):
				for word in sentence[(idx2+1):(idx2+1+DDI_scope)]:
					for positive in positives:
						if word==positive:
							cnt += 1
							break



			if cnt>=1:
				feature3 = 1
			print ("Feature3:",feature3)


			#-> Compute fourth feature i.e count number of negative 
			#   keywords in sentence

			cnt = 0
			for word in sentence:
				for negative in negatives:
					if word==negative:
						cnt += 1
						break

			feature4 = cnt
			print ("Feature4:",feature4)

			#-> Compute fifth feature i.e whether one or more negatives 
			#   exist between the two drug names

			cnt = 0
			feature5 = 0 #check whether feature 5 is true or not
			for word in sentence[idx1+1:idx2]:
				for negative in negatives:
					if word==negative:
						cnt += 1
						break

			if cnt>=1:
				feature5 = 1
			print ("Feature5:",feature5)


			#-> Compute sixth feature i.e whether one or more negative 
			#   exist within scope but not between the two drug names

			cnt = 0
			feature6 = 0 #check whether feature 3 is true or not
			#Check before first drug name
			if ( (idx1+1) > DDI_scope):
				for word in sentence[(idx1-DDI_scope):idx1]:
					for negative in negatives:
						if word==positive:
							cnt += 1
							break

			#Check after second drug name
			if ( (len(sentence)-(idx2+1)) > DDI_scope):
				for word in sentence[(idx2+1):(idx2+1+DDI_scope)]:
					for negative in negatives:
						if word==positive:
							cnt += 1
							break



			if cnt>=1:
				feature6 = 1
			print ("Feature6:",feature6)


			#-> Compute seventh feature i.e number of special
			#	words in the whole sentence

			cnt = 0 #count number of positive keywords
			for word in sentence:
				#print (word)
				for special in specials:
					if word==special:
						cnt += 1
						break

			feature7 = cnt
			print ("Feature7:",feature7)


			#-> Compute eighth feature i.e number of words
			#	in between two drugs

			cnt = 0 #count number of words
			if flags[1] == 1:
				cnt = len(sentence[idx1+1:idx2-1])
			else:
				cnt = len(sentence[idx1+1:idx2])
			
			feature8 = cnt
			print ("Feature8",feature8)

			#-> Compute ninth feature i.e number of verbs
			#	between two drugs

			cnt = 0 #count number of words
			words = pos_tag(sentence)
			for word in words:
				if word[1] == "VB" or word[1] == "VBD" or word[1] == "VBG" or word[1] == "VBN" or word[1] == "VBP" or word[1] == "VBZ":
					cnt += 1


			feature9 = cnt
			print ("Feature9:",feature9)


			class_l = 0
			data = [feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,class_l]
			with open('ML/trainFeatures1.csv','a',newline='') as f:
				wrt = csv.writer(f, delimiter = ',')
				wrt.writerow(data)



#******************************************************** End ************************************************************

		
