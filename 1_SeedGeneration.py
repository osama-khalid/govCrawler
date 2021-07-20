'''
Seed Generation
input: a Top-Level Domain
output: a list of seed domains stored as <tldName>.tldDump.csv
'''

#Example
seed='gov.br'


#-------------------



import requests
import bs4
import time



counter=10
collections=[]
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
headers={"sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',"sec-ch-ua-mobile": "?0","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","X-Client-Data": "CIq2yQEIo7bJAQjBtskBCKmdygEIopbLAQiMnssBCKCgywEIhPLLAQit8ssBCNzyywEI8PLLAQiz+MsBCJb5ywEInvnLAQjy+csBCLD6ywEYuvLLARiQ9csB","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document"}
tld=seed
text= "site:"+tld
k=0
while(counter>4):

    cursor='&start='+str(k)+'&num=100'
    k=k+100
    rootUrl = 'https://google.com/search?q=' + text + cursor

    # Fetch the URL data using requests.get(url),
    # store it in a variable, request_result.
    p=0
    while(1):
        try:
            request_result=requests.get( rootUrl , headers=headers,timeout=20)
            print(rootUrl)
            print(request_result)
            break
        except:
            p=p+1
            print('timeOut',p)
            time.sleep(10*p)

      
    # Creating soup from the fetched request
    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")

    #print(soup)

    # soup.find.all( a href ) to grab 
    # all major headings of our search result,
    heading_object=soup.find_all( 'a', href=True )
    
    # Iterate through the object 
    # and print it as a string.
    counter=0
    for info in heading_object:
        url=info['href']
        #print(url,tld in url)
        if tld in url:
            print(url)
            urlReformed=url.split(tld)[0]+tld
            if 'http' in url:
                counter=counter+1    
            collections.append(urlReformed)
        '''
        if "/url?q=" in url:
            if url.startswith('/url?q='):
                if '//' in url.split('/url?q=')[1]:
                    urlCandidate=url.split('/url?q=')[1].split('//')
                    header=urlCandidate[0]
                    if '/' in urlCandidate[1]:
                        footer=urlCandidate[1].split('/')[0]
                        urlReformed=header+'//'+footer
                        counter=counter+1
                        if tld in urlReformed:
                            print(urlReformed)
                            collections.append(urlReformed)
        '''
    time.sleep(25)

collections=list(set(collections))
c2=[]
for c in collections:
    if '.'+tld in c:
        if c.startswith('http')==True:
            url=c.split('//')[1].split('/')[0]
            if tld in url:
                c2.append(c)
file=open(tld+'.tldDump.csv','w')
file.write('\n'.join(c2))    