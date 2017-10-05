setwd("C:/Users/Risheek/Documents/minor")
library(nnet)
Data = read.csv("trainFeatures3.csv")
data <- as.data.frame(Data[sample(nrow(Data)),]) 
cl<-as.data.frame(data[,(ncol(data))])  
#View(cl)
ttd<-as.data.frame(data[,1:9])
p=380 #for splitting 70:30
b<-nrow(cl)-p+1
#testing
clts<-as.data.frame(cl[b:nrow(cl),])
trs<-as.data.frame(ttd[b:nrow(ttd),])
#neural net the model

cltr<-as.data.frame(cl[1:(b-1),])
#View(cltr)
trr<-as.data.frame(ttd[1:(b-1),])
#trr<-ipnorrm(trr)
View(trr)
data<-data[1:(b-1),]
cltr<-class.ind(data$Class)

NN_net <- nnet(trr, cltr, size =10,rang = 0.1,softmax = TRUE)
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
print(rowsums)
#print(rowsums)
colsums = apply(m, 2, sum)
print(colsums)

accuracy = sum(diag) / n 
accuracy 

precision = diag / colsums 
print(precision)


recall = diag / rowsums 
print(recall)

f1 = 2 * precision * recall / (precision + recall) 
print(f1)
#accuracy

