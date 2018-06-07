
import os,subprocess,time
from crawller import crawller
from bag_of_words_trainer_build5_2 import trainer

pos={}
neg={}
neut={}

cwd=os.getcwd()
resultlocation=cwd+"\\results\\"+""
f1=open(resultlocation+"polarity.txt","r")
p=[]
for i in f1:
    i=i.replace("\n","")
    p.append(i)
f1.close()
f1=open(resultlocation+"dates.txt","r")
d=[]

for i in f1:
    d.append(i)
f1.close()

for i in range(0,len(p)):
    if p[i]=="POSITIVE":
        if pos.has_key(d[i]):
            pos[d[i]]+=1
        else:
            pos[d[i]]=1
    if p[i]=="NEGATIVE":
        if neg.has_key(d[i]):
            neg[d[i]]+=1
        else:
            neg[d[i]]=1
               
    if p[i]=="NEUTRAL":
        if neut.has_key(d[i]):
            neut[d[i]]+=1
        else:
            neut[d[i]]=1

dpos=pos.keys()
dneg=neg.keys()
dneut=neut.keys()
final=[]
k=""
for i in range(0,len(dpos)):
    if pos.has_key(dpos[i]):
        k=k+str(pos[dpos[i]])+"\t"
    else:
        k=k+str(0)+"\t"

    if neg.has_key(dpos[i]):
        k=k+str(neg[dpos[i]])+"\t"
    else:
        k=k+str(0)+"\t"

    if neut.has_key(dpos[i]):
        k=k+str(neut[dpos[i]])+"\t"
    else:
        k=k+str(0)+"\t"
        
    k=k+dpos[i]
    final.append(k)

f2=open(resultlocation+"rinput.txt","w+")
for i in range(0,min(len(d),len(p))):
   f2.write(p[i]+"\t"+d[i])
f2.close()
prev=[]
f2=open(resultlocation+"rinput2.txt","w+")
for i in range(0,len(final)):
   x=final[i].split()
   if x[3] not in prev:
       f2.write(final[i])
       prev.append(final[i])
f2.close()


print "-------------FIN---------------"
time.sleep(2)
ret=subprocess.call("x.R",shell=True)
