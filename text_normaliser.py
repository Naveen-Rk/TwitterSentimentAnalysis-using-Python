# -*- coding: utf-8 -*-


class text_filter:
    
    def __init__(self):
        self.found=["don't","can't","won't","should'nt","would'nt","could'nt","cant","wont","dont","@","&","wer'nt","wernt","thell",".","\n","-","_","/n","[","]","'","{","}","|","(",")","#","$","%",",","?"]
        self.change=["do not","can not","would not","should not","would not","could not","can not","would not","do not","at","and","wer not","wer not","they will",""]
        
    def fil(self,s):
        s=s.lower()
        for i in range(0,len(self.found)):
            if i <= 13 :
                s=s.replace(self.found[i],self.change[i])
            else:
                s=s.replace(self.found[i],self.change[-1])
        return s
    
def main():
    obj=text_filter()
    s=raw_input("inp: ")
    ans=obj.fil(s)
    print "\n"+ans
    
#main()