
from sets import Set



class grouper:
    def __init__(self):
	
	
		self.cwd=os.getcwd()
		#self.cwd=self.cwd.replace('\',"\\\\")
		self.trainlocation=self.cwd+"\\trainingdata\\"
		self.resultlocation=self.cwd+"\\results\\"
        
	
	
	
	
	
        self.n_items=Set()
        self.first="and, any, anyone, anything, are, be, best, can, cannot, cant, can't, could, couldn't, did, didn't, do, does, doesn't, done, don't, either, else, even, every, for, from, have, haven't, he's, is, isn't, it, its, i've, just, like, lots, many, maybe, me, might, more, must, my, never, no, none, not, nothing, now, of, on, once, one, only, or, overly, perfectly, perhaps, probably, seemed, seems, she's, should, simply, so, some, somehow, something, soon, start, takes, tell, thank, that's, the, their, them, then, there, there's, they, they're, this, those, to, too, totally, tried, truly, try, turns, until, upon, use, very, wait, was, well, went, were, whether, which, whole, why, will, wish, won't, would, wouldn't, you, you'll, your, you're, yourself "
        self.first=self.first.split(", ")
        self.n_items.update(self.first)
        self.words=[]
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
        for i in self.first:
            if i in new_arr:
                del(new_arr[new_arr.index(i)])
        return new_arr       

def main():
    obj=grouper()
    input_str=raw_input("input :").split()
    ans=obj.group(input_str)
    print ans

#main()