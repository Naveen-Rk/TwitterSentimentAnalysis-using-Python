library(lattice)
t<-read.table(file="C:\\Users\\Sabari\\Documents\\LiClipse Workspace\\TwitterSentimentAnalysis\\results\\rinput.txt",sep="\t",header=FALSE)
t$V2<-as.Date(t$V2,format="%m/%d/%y")
t2<-read.table(file="C:\\Users\\Sabari\\Documents\\LiClipse Workspace\\TwitterSentimentAnalysis\\results\\rinput2.txt",sep="\t",header=FALSE)
colnames(t2)<-c("POSITIVE","NEGATIVE","NEUTRAL","DATE")

t2$V4<-as.Date(t2$DATE,format="%m/%d/%y")
d<-t2[order(t2$V4),]

rel<-unique(d[,1:4])
myt<-table(t$V1)


rel$DATE<-as.Date(rel$DATE,format="%m/%d/%y")

show(rel)


plot(y=rel$NEGATIVE,x=rel$DATE,type="o",col="red",ylim = c(0,max(rel$NEGATIVE)))
lines(y=rel$POSITIVE,x=rel$DATE,type="o",col = "green")
lines(y=rel$NEUTRAL,x=rel$DATE,type='o',col = "blue")

plot(t$V1)
pie(myt,main = "Pie Chart")