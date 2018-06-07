from sets import Set
import os


class grouper:
    #load stop words 
    def __init__(self):
        self.cwd=os.getcwd()
        self.trainlocation=self.cwd+"\\training_data\\"
        self.resultlocation=self.cwd+"\\results\\"
        self.words=[]
        
        self.n_items=Set()
        f=open("F:\\PROJECT\\training_data\\stop_words.txt","r")
        self.first=[]
        for i in f:
            i=i.replace("\n","")
            self.first.append(i)
        f.close()
        self.n_items.update(self.first)

        
        
        
        f=open(self.trainlocation+"stop_words.txt","r")
        for i in f:
            i=i.replace("\n","")
            self.words.append(i)
        f.close()
        
        
        
    def group(self,a):
        
        new_arr=[]
        temp=""
        for i in range(0,len(a)):
                      
            if a[i] not in self.n_items:
                if temp != "":
                    new_arr.append(temp+" "+a[i])
                    #print "->",temp
                    temp=""
                    #print temp
                else:
                    
                    new_arr.append(a[i])
            else:
                if i<(len(a)-1):
                    #print a[i],"t:",temp
                    if temp !="":
                        if a[i]=="and" and len(new_arr)>0:
                            x=new_arr.pop()
                            temp=x+" "+a[i]
                        else:
                            temp=temp+" "+a[i]
                    else:
                        if a[i]=="and" and len(new_arr)>0:
                            x=new_arr.pop()
                            temp=x+" "+a[i]
                        else:
                            temp=a[i]
                    
                else:
                    
                    if temp=="":
                        new_arr.append(a[i])
                    else:
                        new_arr.append(temp+" "+a[i])
        
        for i in self.words:
            if i in new_arr:
                del(new_arr[new_arr.index(i)])
        return new_arr       

def main():
    obj=grouper()
    input_str=raw_input("input :").split()
    ans=obj.group(input_str)
    print ans

#main()