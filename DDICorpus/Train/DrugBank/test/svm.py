import random
import math
import csv
import numpy
from sklearn import svm
from sklearn.model_selection import train_test_split
import random
import pandas as pd
import numpy as np
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.metrics import precision_score

data_path = "/home/kevmepls/Documents/IR/APIforDDICorpus/DDICorpus/Train/DrugBank/ML/"

data = pd.read_csv(data_path+"trainFeatures3.csv", header=0, delimiter=",")

#print (type(data))
#print (data[0])
df = pd.DataFrame(data)
#print (df["F1"][1])
#print (df.columns)

new_train = df.reindex(np.random.permutation(df.index))
length = len(new_train)
#print (length)
train_idx = int(float(0.7) * len(new_train))

train_data = new_train[0:train_idx] 
test_data = new_train[train_idx:]

#print (train_data.iloc[:,9:])

#-> Slicing data by choosing first 8 columns
#   as input features
train_data_x = train_data.iloc[:,0:9]

#-> Slicing data by choosing last column
#   as class label

train_data_y = train_data.iloc[:,9:]

#print (type(train_data_y))
#train_data_y = train_data_y.ravel()
#print (type(train_data_y))

test_data_x = test_data.iloc[:,0:9]
test_data_y = test_data.iloc[:,9:]


#print (test_data_x.values)
#print (train_data['Class'])
#print (train_data['F1,F9'])

#print (len(train_data))
#print (len(test_data))	


train_data_x = train_data_x.squeeze()
train_data_y = train_data_y.squeeze()

#train_data_x = np.array(train_data_x)
#train_data_y = np.array(train_data_y)


clf=svm.SVC(kernel='linear', C = 1.7)
clf.fit(train_data_x,train_data_y)
#print ("Sc:",clf.score(test_data_x, test_data_y)*100)


#Compute scores	
#print (len(test_data_y))
y_pred = []
y_pred = clf.predict(test_data_x)

idx = 0
#for index, row in test_data_x.iterrows():
#	print (row)

print ( "Accuracy:", accuracy_score(test_data_y, y_pred) )
print ( "Recall:", recall_score(test_data_y, y_pred) )
print ( "Precision:", precision_score(test_data_y, y_pred) )
print ( "F-Measure:", f1_score(test_data_y, y_pred) )

joblib.dump(clf, 'SVM2.pkl')

#for i in range(383):
	#actaul_y_pred.append( clf.predict([test[i]]) )

#print ("Sc:",clf.score(X_test, y_test))

