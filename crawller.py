from progressbar import ProgressBar
import time,os
import urllib3,json,requests
from bs4 import BeautifulSoup

class crawller:
    def __init__(self):
        self.months=["Jan","Frb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        self.cwd=os.getcwd()
        self.trainlocation=self.cwd+"\\training_data\\"+""

        self.resultlocation=self.cwd+"\\results\\"+""
    	  
        i_url="https://twitter.com/search.json?q="                 #initial search template
        topic=raw_input("Enter the topic you wanna search: ")      #user's topic
        topic=topic.replace(' ','%20').replace('#','%23')          #handling spaces and #tags
        pages=input("Enter no of tweets needed :")
        pages=(pages/20)+1
        f_url=i_url+topic+"&src=typd"                              #final first url to send

        r=urllib2.urlopen(f_url)                                   #open webpage
        html=r.read()                                              #extract html content
        all_tweets={}
        
        #template for reload
        RELOAD_URL = "https://twitter.com/i/search/timeline?f=tweets&vertical=" \
                     "default&include_available_features=1&include_entities=1&" \
                     "reset_error_state=false&src=typd&max_position={pos}&q={q}"
        
        
        soup=BeautifulSoup(html)                                                        #parse html doc
        x=soup.find_all("li",{"class":"js-stream-item stream-item stream-item "})       #extract tweet from web document which is under  class js-stream
        [s.extract() for s in soup('a')]                                                #remove <a> tag contents from tweet
        
        
        var=time.time()
        #step to get next tweet-id to querry for scroll automation
       
        for i in x:
            j=i.get("id")
            j=j.split('-')
        

        print("done first part ..starting XHR querry and crawling ")
        print("this process takes time please wait ... ")
        bar=ProgressBar()
        #auto scroll and extraction of new tweets
        for i in bar(range(0,pages+1)):
            n="https://twitter.com/i/search/timeline?f=tweets&vertical=default&include_available_features=1&include_entities=1&reset_error_state=false&src=typd&max_position="+j[3]+"&q="+topic+"&src=typd"
            #rerequesting
            r=requests.get(n)
            html=r.text
            
           
            #get json response from web page and extaracts only the html elements from it
            js=r.json()
            lattex=js['items_html']
            #assing html elements for parsing
            soup2=BeautifulSoup(lattex,"lxml")
            
            #print soup2
            
            for tweet  in soup2.find_all("div", {"class":"content"}):
                if(tweet.find("a",{"class":"tweet-timestamp"})):
                    temp1= tweet.find("a",{"class":"tweet-timestamp"}).get("title")
                    [s.extract() for s in tweet('a')]
                    if tweet.find("p",{"class":"TweetTextSize js-tweet-text tweet-text"}):
                        if tweet.find("p",{"class":"TweetTextSize js-tweet-text tweet-text"}).get("lang") == "en":
                            temp2= tweet.find("p",{"class":"TweetTextSize js-tweet-text tweet-text"}).text
                            all_tweets[temp2]=temp1
            

        j[3]=js['min_position']
        print ("done whth gathering tweets ## total gathered= ",len(all_tweets))
        #works able to querry for new tweets
        print ("---------------")

        j=0
        
        
        f=open(self.resultlocation+"pol.txt","w+")
        f2=open(self.resultlocation+"dates.txt","w+")
        key= all_tweets.keys()
        for i in key:
            temp=all_tweets[i]
            temp=temp.split()
            
            
            conv=self.months.index(temp[4])+1
            date=str(conv)+"/"+temp[3]+"/"+temp[5][2:]
            f2.write(date+"\n")
            
            i=i.replace("\n","")
            i=i.encode("utf8")
            f.write(i+"\n")
        f.close()
        f2.close()
        
        
         
        print ("Time taken : ",time.time()-var)
        print("----------FIN------------")


obj=crawller()
