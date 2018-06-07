
'''
This program performs all the sentimental analysis 
'''
import os
from bag_of_words_grouper2 import grouper
from text_normaliser import text_filter
from stop_word_remover import rem

class trainer:
    
    
    def __init__(self):#initialize vars and load positive and negative words of wordgram
        self.pos={}
        self.neg={}
        self.uni_pos={}
        self.uni_neg={}
        self.positive=[]
        self.negative=[]
        self.total_uni=[0,0]
        self.total_ngram=[0,0]
        self.cwd=os.getcwd()
        self.trainlocation=self.cwd+"\\training_data\\"+""
        self.resultlocation=self.cwd+"\\results\\"+""
        f=open(self.trainlocation+"positive-words.txt","r")
        #positive words 2007 in total
        for i in f:
            i=i.replace("\n","")
            self.positive.append(i)
        f.close()
        
        f=open(self.trainlocation+"negative-words.txt","r")
        #negative words 4784 in total 
        for i in f:
            i=i.replace("\n","")
            self.negative.append(i)
        
        
    
    def train_pos(self):#ngram positive case training
        
        train=grouper()
        obj=text_filter()
        f=open(self.trainlocation+"rt-polarity.pos","r")
        for i in f:
            i=obj.fil(i)
            i=i.split()
            
            
            temp=train.group(i)
            for j in temp:
                if self.pos.has_key(j):
                    self.pos[j]+=1
                    self.total_ngram[0]+=1
                else:
                    self.pos[j]=1
                    self.total_ngram[0]+=1
        f.close()
        f=open(self.resultlocation+"pos-count.txt","w+") #save ngram pos bag 
        key=self.pos.keys()
        value=self.pos.values()
        for i in range(0,len(key)):
            s=key[i]+"     "+str(value[i])+"\n"
            f.write(s)
        f.close()
        print "done positive"
        
    def train_neg(self):#ngram negative case training
        
        train=grouper()
        obj=text_filter()

        f=open(self.trainlocation+"rt-polarity.neg","r")
        for i in f:
            i=obj.fil(i)
            i=i.split()
           
            
            temp=train.group(i)
            for j in temp:
                if self.neg.has_key(j):
                    self.neg[j]+=1
                    self.total_ngram[1]+=1
                else:
                    self.neg[j]=1
                    self.total_ngram[1]+=1
        f.close()
        f=open(self.resultlocation+"neg_count.txt","w+")
        key=self.neg.keys()
        value=self.neg.values()
        for i in range(0,len(key)):
            s=key[i]+"     "+str(value[i])+"\n"
            f.write(s)
        f.close()
        print "done negative"   
        
    
    def unigram_train(self):#trainer for unigram
        obj=rem()
        f=open(self.trainlocation+"rt-polarity.pos","r")
        for i in f:
            string=obj.fil(i)
            string=string.split()
            for j in string:
                if self.uni_pos.has_key(j):#dictionary stroes wordcount O(1) for all operations
                    self.uni_pos[j]+=1
                    self.total_uni[0]+=1
                else:
                    self.uni_pos[j]=1
                    self.total_uni[0]+=1
        f.close()
        f=open(self.resultlocation+"uni_pos_count.txt","w+") #contains unigram positive word count 
        key=self.uni_pos.keys()
        value=self.uni_pos.values()
        for i in range(0,len(key)):
            s=key[i]+"     "+str(value[i])+"\n"
            f.write(s)
        f.close()
        
        f=open(self.trainlocation+"rt-polarity.neg","r")
        for i in f:
            string=obj.fil(i)
            string=string.split()
            for j in string:
                if self.uni_neg.has_key(j):
                    self.uni_neg[j]+=1
                    self.total_uni[1]+=1
                else:
                    self.uni_neg[j]=1
                    self.total_uni[1]+=1
        f.close()
        f=open(self.resultlocation+"uni_neg_count.txt","w+") #contains unigram negative word count
        key=self.uni_neg.keys()
        value=self.uni_neg.values()
        for i in range(0,len(key)):
            s=key[i]+"     "+str(value[i])+"\n"
            f.write(s)
        f.close()
    
    def unigram(self,string):# inp is a string ,performs count comparision with normalization
        pos=0
        neg=0
        neut=0
        print "unigram inp: ",string
        string=string.split()
        for i in string:
            if self.uni_pos.has_key(i) or self.uni_neg.has_key(i):
                if self.uni_pos.has_key(i):
                    pos+=self.uni_pos[i]
                if self.uni_neg.has_key(i):
                    neg+=self.uni_neg[i]
            else:
                neut+=1
        c_pos=float(pos)/self.total_uni[0]
        c_neg=float(neg)/self.total_uni[1]
        
        print "unigram   P:",c_pos,"N: ",c_neg,"neut: ",neut
        print " "
        if neut!=0 and (c_pos==0 and  c_neg==0 or (c_pos==c_neg)):
            return "NEUTRAL"
        else:
            if c_pos > c_neg:
                return "POSITIVE"
            else:
                return "NEGATIVE"
        
    
    
    
    def ngram(self,arr):#inp is an array performs dynamic ngramming and finds polarity
        
        pos=0
        neg=0
        neut=0
        print "ngram inp: ",arr
        for i in arr:
            
            if self.pos.has_key(i) and self.neg.has_key(i):
                
                pos+=self.pos[i]
                neg+=self.neg[i]
                
            else:
                if self.pos.has_key(i):
                    
                    pos+=self.pos[i]
                elif self.neg.has_key(i):
                    
                    neg+=self.neg[i]
                else:
                    
                    neut+=1
        print "ngram   P:",pos,"N: ",neg,"neut: ",neut
        print" "
        if (neut > pos and neut > neg) or pos==neg:
            return "NEUTRAL"
        else:
            if pos > neg:
                return "POSITIVE"
            else:
                return "NEGATIVE"
                
    
    def wordgram(self,arr):    
        pos=0
        neg=0
        
        print "wordgram inp: ",arr
        for  i in arr:
            index=arr.index(i)
            if (i=="not" or i=="nor") and index+1 < len(arr):
                
                for x in arr[index+1:]:
                    if x in self.positive:
                    #print "not (+)"
                        neg+=2
                        break
                
                    if x in self.negative:
                    #print "not (-)"
                        pos+=2
                        break
            else:  
            
                if i in self.positive:
                    pos+=1
                elif i in self.negative:
                    neg+=1

                            
        print "wordgram  P:",pos,"N:",neg    
        print " "        
        if pos==neg:
            return "NEUTRAL"
        else:
            if pos > neg:
                return "POSITIVE"
            else:
                return "NEGATIVE"
     

        
        
            
        
        
    
    def test(self):#primary function which performs polarity check
        obj=grouper()
        obj2=text_filter()
        obj3=rem()
        answer=[]
        
        while(True):
            '''Load the text file which has sentences to perform sentimental analysis here
                                |             |                |
                                V             V                V
            '''
            
            f=open(self.resultlocation+"pol.txt","r")  #tweets
            
            
            for  s in f:
                
                
                s=obj2.fil(s)
                s_arr=s.split()
                if s=="exit" :
                    break
                if len(s_arr)>1 and ((s_arr[0]=="what" and s_arr[-1]=="?") or (s_arr[0]=="how" and s_arr[-1]=="?")):
                    print "You entered a question"
                
                else:
                    
                    s1=obj3.fil(s)
                    ans=obj.group(s_arr)
                    
                    ngram_opt=self.ngram(ans)
                    wordgram_opt=self.wordgram(s_arr)
                    unigram_opt=self.unigram(s1)
                    
                    
                    print"Comparision: "
                    print "wordgram="+wordgram_opt+"    "+"ngram="+ngram_opt+"   "+"unigram="+unigram_opt
                    
                    if ngram_opt==wordgram_opt==unigram_opt:
                        print ngram_opt
                        answer.append(ngram_opt)
                        
                    else:
                        
                        if wordgram_opt == "NEUTRAL":
                            if ngram_opt==unigram_opt:
                                print ngram_opt
                                answer.append(ngram_opt)
                            else:
                                if ngram_opt=="NEUTRAL" or unigram_opt=="NEUTRAL":
                                    print "NEUTRAL"
                                    answer.append("NEUTRAL")
                                elif ngram_opt=="POSITIVE" and unigram_opt=="NEGATIVE":
                                    print "not sure could be -> ",unigram_opt
                                    answer.append(ngram_opt)
                                elif ngram_opt=="NEGATIVE" and unigram_opt=="POSITIVE":
                                    print "not sure could be -> ",ngram_opt
                                    answer.append(ngram_opt)
                                
                        
                        elif wordgram_opt == "POSITIVE":
                            if ngram_opt == unigram_opt:
                                print ngram_opt
                                answer.append(ngram_opt)
                            
                            else:
                                if ngram_opt=="NEUTRAL":
                                    if unigram_opt=="NEGATIVE":
                                        print "not sure could be -> ",wordgram_opt
                                        answer.append(wordgram_opt)
                                        
                                    elif unigram_opt=="POSITIVE":
                                        print "POSITIVE"
                                        answer.append("POSITIVE")
                                
                                elif unigram_opt=="NEUTRAL":
                                    if ngram_opt=="POSITIVE":
                                        print "POSITIVE"
                                        answer.append("POSITIVE")
                                    elif ngram_opt=="NEGATIVE":
                                        print "not sure coild be -> ",ngram_opt
                                        answer.append(ngram_opt)
                                else:
                                    if ngram_opt=="POSITIVE" or unigram_opt=="POSITIVE":
                                        print "POSITIVE"
                                        answer.append("POSITIVE")
                                    
                        else:#wordgram_opt==NEGATIVE
                            if ngram_opt == unigram_opt:
                                print ngram_opt
                                answer.append(ngram_opt)
                            
                            else:
                                if ngram_opt=="NEUTRAL":
                                    if unigram_opt=="POSITIVE":
                                        print "not sure could be -> ",wordgram_opt
                                        answer.append(wordgram_opt)
                                    elif unigram_opt=="NEGATIVE":
                                        print "NEGATIVE"
                                        answer.append("NEGATIVE")
                                elif unigram_opt=="NEUTRAL":
                                    if ngram_opt=="NEGATIVE":
                                        print "NEGATIVE"
                                        answer.append("NEGATIVE")
                                    elif ngram_opt=="POSITIVE":
                                        print "not sure coild be -> ",wordgram_opt
                                        answer.append(wordgram_opt)
                                else:
                                    if ngram_opt=="NEGATIVE" or unigram_opt=="NEGATIVE":
                                        print "NEGATIVE"
                                        answer.append("NEGATIVE")
            
            break
        '''
        Displays total case polarity 

        '''         
        print "Positive: ",answer.count("POSITIVE")
        print "Negative: ",answer.count("NEGATIVE")
        print "Neutral: ",answer.count("NEUTRAL")
        f2=open(self.resultlocation+"polarity.txt","w+")
        for i in answer:
            f2.write(i+"\n")
        f2.close()
                        
                    
        
                         
def main():
    
    obj=trainer()
    obj.train_pos()
    obj.train_neg()
    obj.unigram_train()
    pop=[ obj.total_uni[0],obj.total_uni[1]]
    
    obj.test()
    #print pop
    
main()