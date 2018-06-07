
import os
class rem:
    
    def __init__(self):
        self.cwd=os.getcwd()
        #self.cwd=self.cwd.replace('\',"\\\\")
        self.trainlocation=self.cwd+"\\training_data\\"
        self.resultlocation=self.cwd+"\\results\\"
        self.words=[]
        f=open(self.trainlocation+"stop_words.txt","r")
        for i in f:
            i=i.replace("\n","")
            self.words.append(i)
        
        f.close()
        
    
    def fil(self,s):
        s=s.lower()    #change all characters to lower case 
        s=s.split()    #split a sentence into an array based on " " 
        for i in self.words:
            while True:
                if i not in s:
                    break
                else:
                    del(s[s.index(i)])  #stop word is removed from the array
        x=""
        for m in range(0,len(s)):
            x=x+s[m]+" "
        return x
    
def main():
    obj=rem()
    s=raw_input("inp: ")
    ans=obj.fil(s)
    
    print "\n"+ans
    
#main()