'''
Search Expansion using Breadth-First Search
input: a Top-Level Domain
output: starting from the seeds from <tldName>.tldDump.csv, crawls 
all the links until it has downloaded 1 million pages and stored them in <tldName>.Data.csv
'''


#Example1
topLevelDomain='gov.br'

#Example2
topLevelDomain='gob.ar'

pageCount=1000000
#------------------------
import requests
import bs4
import re
import time
import html
import csv
pattern = '<[ ]*script.*?\/[ ]*script[ ]*>'
HASHSET=[]
root=topLevelDomain
file=open(root+'.tldDump.csv','r').read().split('\n')
file2=[]
R={}
dictionary={}
for f in file:
    file2.append(f+'/')
headers={"sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',"sec-ch-ua-mobile": "?0","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","X-Client-Data": "CIq2yQEIo7bJAQjBtskBCKmdygEIopbLAQiMnssBCKCgywEIhPLLAQit8ssBCNzyywEI8PLLAQiz+MsBCJb5ywEInvnLAQjy+csBCLD6ywEYuvLLARiQ9csB","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document"}

Data=[]
queue={}
for f in file2:
    queue[f]=0
queue2=[]
flag=0
queue2.extend(file2)
request_result=[]
import random
STOP=0
with open(root+'.Data.csv',mode='w',encoding='utf-8') as urduDic:
    foodWrite=csv.writer(urduDic,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    
    while len(queue2)>0 and STOP<pageCount:
        p=0
        #random.shuffle(queue2)
        q=queue2.pop(0)
        cnt=queue[q]
        if cnt>5:
            flag=1
        q=q.strip('/')
        q=q.lower()
        temp=q.strip('/').split('.')
        if q.startswith('http')==True and q.find('.jpg')==-1 and q.find('.rar')==-1 and q.find('.zip')==-1 and q.find('.doc')==-1 and q.find('.xls')==-1 and q.find('.ppt')==-1   and q.find('.jpeg')==-1 and q.find('.png')==-1 and q.find('.svg')==-1 and q.find('.pdf')==-1 and q.find('.mp3')==-1 and q.find('.mp4')==-1 and q.endswith('.jsp')!=True and q.endswith('.php')!=True:
            if '//' in q:
                core=q.split('//')[1].split('/')[0]
                if 'www.' in core:
                    core=core.split('www.')[1]
                print('pages in queue')
                print(len(queue2),q)
                while(1):
                    try:
                        request_result=requests.get(q, headers=headers,timeout=5,allow_redirects=False)
                        print(q)
                        #print(request_result,cnt)
                        row=[]
                        row.append(q)

                        if type(request_result)!=type(row) and '<body' in request_result.text and '/body>' in request_result.text:
                            txt='<body'+request_result.text.split('<body')[1].split('/body>')[0].replace('\0','')+'/body>'
                            cleantext=re.sub('<[^>]*>', ' ', txt)
                            cleantext=html.unescape(cleantext)
                            cleantext = re.sub(pattern, '', cleantext, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
                            cleantext=cleantext.replace('\n',' ').replace('\r',' ').replace('\t',' ')
                            while('  ' ) in cleantext:
                                cleantext=cleantext.replace('  ',' ')
                            row.append(cleantext)
                            
                            if hash(row[1]) not in HASHSET:
                                HASHSET.append(hash(row[1]))
                                if len(request_result.text)>2:
                                    
                                    foodWrite.writerow(row)
                                    STOP=STOP+1
                        soup = bs4.BeautifulSoup(request_result.text,
                                                 "html.parser")

                        #print(soup)

                        # soup.find.all( a href ) to grab 
                        # all major headings of our search result,
                        try:
                            heading_object=soup.find_all( 'a', href=True )
                            
                            # Iterate through the object 
                            # and print it as a string.
                            counter=0
                            for info in heading_object:
                                url=info['href']
                                if len(url)>0:
                                    if url[0]=='/':
                                        rootU=q.split('//')
                                        newRoot=rootU[0]+'//'+rootU[1].split('/')[0]
                                        if newRoot not in R:
                                            R[newRoot]=[]
                                        if url not in R[newRoot]:
                                            R[newRoot].append(url)
                                            url=newRoot+url

                                if core in url and root in url and len(q)<100:
                                    if url not in queue:
                                        queue[url]=cnt+1
                                        queue2.append(url)
                        except:
                            continue




                        break
                    except:
                        p=p+1
                        print('timeOut',p)
                        if p>3:
                            break
                        time.sleep(1)
                
            