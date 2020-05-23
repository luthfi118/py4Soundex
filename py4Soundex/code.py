import re
def Soundex(x):
    x=x.lower()
    first_char=x[0]
    temp=x[1:]
    temp=re.sub("[aeiouyhw]","",temp)
    if(len(temp)==0):
        first_char=first_char+"000"

    temp=re.sub("[bfpv]","1",temp)
    temp=re.sub("[cgjkqsxz]","2",temp)
    temp=re.sub("[dt]","3",temp)
    temp=re.sub("[l]","4",temp)
    temp=re.sub("[mn]","5",temp)
    temp=re.sub("[r]","6",temp)

    temp=[x for ind,x in enumerate(temp) if(ind==len(temp)-1 or (ind+1<len(temp) and x !=temp[ind+1])) ]

    if(temp[0]==first_char):
        temp[0]=x[0]
    else:
        temp.insert(0,x[0])

    if(len(temp)<=3):
        temp.append("0")
        temp.append("0")
        temp.append("0")
    temp=temp[0:4]
    temp="".join(temp)
    return temp
