#snpdistance
import sys
from collections import OrderedDict
goin = sys.argv[1]
goout = sys.argv[2]

fr=open(goin, 'r')
fw=open(goout, 'w') 
dict = OrderedDict()
for line in fr:
    if line.startswith('>'):
        name=line.strip()[1:]
        #print(name)
        dict[name]=''
    else:
        dict[name]+=line.replace('\n','').strip()
        
temp = list(dict.keys())
print(temp)
print(len(temp))
lock = 0

for i in temp:
    lock += 1
    for j in range(len(temp)):
        t = 0
        if j+1 > len(temp):
            break
        else:
            for k in range(len(dict[temp[j]])):
                if k+1 > len(dict[temp[j]]) - 2:
                    break
                else:
                    if dict[i][k] != dict[temp[j]][k] and dict[i][k+1] == dict[temp[j]][k+1]:
                        if dict[i][k] != "-" and dict[temp[j]][k] != "-" :
                            t = t + 1                       
            #print(t,end = ",")        
            print(t,end = ",",file = fw)
    print(i)
    print(i,file = fw)

fr.close()
fw.close()    