# Detecting-drug-drug-interactions


## Preprocessing

From the xml dataset, we have to extract xml tags where the sentence describes only two drugs interacting,
Run :
```
python 3childextrac.py
```

Next, we have to seperate the interactions as either negative or positive so that we can later generate the feature vector dataset with the class labels easily.
Run: 
```
python 2drugsextracpos.py 
```
which will place the positive DDIs into positive folder.


Run :
```
python 2drugsextracneg.py 
```
which will place the negative DDIs into negative folder.

Now we need to compute the feature vector for each sentence.
Run: 
```
python feacompu.py 
```
to compute from positive folder.

Run: 
```
python feacompu_neg.py 
```
to compute from negative folder.

## Machine Learning

KNN and SVM are implemented using scikit learn of python pipeline.
To run above models,go to /DDICorpus/Train/Drugbank or /DDICorpus/Test/Drugbank and run below commands.

```
python svm.py
python knn.py
```

Neural networks and Naive Bayes was implemented in R.
To run neural networks, go to R-Code folder, open nnetfin.R in RStudio and execute it.
To run the final trained NN model, open nnetfin3.R in RStudio and execute it.




## Datasets

The datasetsa are located at DDICorpus/Train/DrugBank/ML/.
