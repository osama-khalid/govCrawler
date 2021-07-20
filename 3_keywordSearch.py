'''
Keyword Search
input: keywords, that can be separated by OR, AND
output: prints stats
'''


#Example 1
keywords='argentina AND colombia'

#Example 2
keywords='gestión del conocimiento OR knowledge management'

#Example 3
keywords='gestión del conocimiento'

#------------------------------------------------------------

import os
import sys
import csv
import re
csv.field_size_limit(sys.maxsize)

root='.Data.csv'
x=0
y=0
dataSet=[]
files=os.listdir('.')
for f in files:
    if root in f:
        dataSet.append(f)
print('Domain'+'\t|\t'+'Total Pages'+'\t|\t'+'TotalSubdomains'+'\t|\t'+'RelevantPages'+'\t|\t'+'RelevantSubdomains'+'\t|\t'+'PercentageSubdomains'+'\t|\t'+'PercentagePages')
       
if keywords.find(' OR ')>-1:
    words=keywords.split(' OR ')
    for d in dataSet:       
        totalPages=0
        totalSubdomains=[]
        relevantPages=0
        relevantSubdomains=[]

        with open(d, 'r',encoding='utf-8') as csv_file:
            csv_reader = csv.reader( (line.replace('\0','') for line in csv_file),delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL )
            #csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            #data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
            for row in csv_reader:
                text=re.sub("[\(\[].*?[\)\]]", "", row[1])
                text=re.sub(r'[^\w\s]','',text)
                #print(len(text))
                end=row[0].split('//')[1].split('/')[0]
                start=row[0].split('//')[0]
                subdomain=start+'//'+end

                cnt=0
                for w in words:
                    if ' '+w.lower().strip(' ') in ' '+text.lower().replace('\n',' ').replace('<br>',' ').replace('\t',' ')+' ':
                        cnt=1
                if cnt==1:
                    relevantPages=relevantPages+1
                    relevantSubdomains.append(subdomain)    
                totalPages=totalPages+1
                totalSubdomains.append(subdomain)
        print('.'.join(d.split('.')[:2])+'\t|\t'+str(totalPages)+'\t\t|\t'+str(len(set(totalSubdomains)))+'\t\t|\t'+str(relevantPages)+'\t\t|\t\t'+str(len(set(relevantSubdomains)))+'\t\t|\t\t'+str(round(100*len(set(relevantSubdomains))/len(set(totalSubdomains)),3))+'%'+'\t\t|\t'+str(round(100*relevantPages/totalPages,3))+'%')


elif keywords.find(' AND ')>-1:
    words=keywords.split(' AND ')
    for d in dataSet:       
        totalPages=0
        totalSubdomains=[]
        relevantPages=0
        relevantSubdomains=[]
        with open(d, 'r',encoding='utf-8') as csv_file:
            csv_reader = csv.reader( (line.replace('\0','') for line in csv_file),delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL )
            #csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            #data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
            for row in csv_reader:
                text=re.sub("[\(\[].*?[\)\]]", "", row[1])
                text=re.sub(r'[^\w\s]','',text)
                #print(len(text))
                end=row[0].split('//')[1].split('/')[0]
                start=row[0].split('//')[0]
                subdomain=start+'//'+end

                cnt=0
                for w in words:
                    if ' '+w.lower().strip(' ') in ' '+text.lower().replace('\n',' ').replace('<br>',' ').replace('\t',' ')+' ':
                        cnt=cnt+1
                if cnt==len(words):
                    relevantPages=relevantPages+1
                    relevantSubdomains.append(subdomain)    
                totalPages=totalPages+1
                totalSubdomains.append(subdomain)

        print('.'.join(d.split('.')[:2])+'\t|\t'+str(totalPages)+'\t\t|\t'+str(len(set(totalSubdomains)))+'\t\t|\t'+str(relevantPages)+'\t\t|\t\t'+str(len(set(relevantSubdomains)))+'\t\t|\t\t'+str(round(100*len(set(relevantSubdomains))/len(set(totalSubdomains)),3))+'%'+'\t\t|\t'+str(round(100*relevantPages/totalPages,3))+'%')
else:
    words=keywords

    for d in dataSet:       
        totalPages=0
        totalSubdomains=[]
        relevantPages=0
        relevantSubdomains=[]

        with open(d, 'r',encoding='utf-8') as csv_file:
            csv_reader = csv.reader( (line.replace('\0','') for line in csv_file),delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL )
            #csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            #data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
            for row in csv_reader:
                text=re.sub("[\(\[].*?[\)\]]", "", row[1])
                text=re.sub(r'[^\w\s]','',text)
                #print(len(text))
                end=row[0].split('//')[1].split('/')[0]
                start=row[0].split('//')[0]
                subdomain=start+'//'+end

                cnt=0
                
                if ' '+words.lower().strip(' ') in ' '+text.lower().replace('\n',' ').replace('<br>',' ').replace('\t',' ')+' ':
                    cnt=1
                if cnt==1:
                    relevantPages=relevantPages+1
                    relevantSubdomains.append(subdomain)    
                totalPages=totalPages+1
                totalSubdomains.append(subdomain)
        print('.'.join(d.split('.')[:2])+'\t|\t'+str(totalPages)+'\t\t|\t'+str(len(set(totalSubdomains)))+'\t\t|\t'+str(relevantPages)+'\t\t|\t\t'+str(len(set(relevantSubdomains)))+'\t\t|\t\t'+str(round(100*len(set(relevantSubdomains))/len(set(totalSubdomains)),3))+'%'+'\t\t|\t'+str(round(100*relevantPages/totalPages,3))+'%')

