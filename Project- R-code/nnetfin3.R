setwd("C:/Users/Risheek/Documents/minor")
library(nnet)
Data = read.csv("trainFeatures4.csv")
data <- as.data.frame(Data[sample(nrow(Data)),]) 
cl <- as.data.frame(data[,(ncol(data))])  
#View(cl)
ttd<-as.data.frame(data[,1:9])
#p=20
b<-1
clts<-as.data.frame(cl[b:nrow(cl),])
trs<-as.data.frame(ttd[b:nrow(ttd),])
#loading the model
NN_net <- readRDS("./final_model.rds")
yPred <- predict(NN_net,trs,type="class")
yPred<-as.data.frame(yPred)
colnames(clts)<-c("Class")
colnames(yPred)<-c("Class")

clts<-unlist(clts)
yPred<-unlist(yPred)
m=as.matrix(table(Actual = clts, Predicted = yPred))

m
n=sum(m)
diag = diag(m)
rowsums = apply(m, 1, sum) # number of instances per class
#print(rowsums)
colsums = apply(m, 2, sum)
#print(colsums)

accuracy = sum(diag) / n 
accuracy 

precision = diag / colsums 
print(precision)


recall = diag / rowsums 
print(recall)

f1 = 2 * precision * recall / (precision + recall) 
print(f1)
#accuracy
