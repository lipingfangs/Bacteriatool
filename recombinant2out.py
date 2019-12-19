#fastGear后接同源区域去除
import sys 
goin = sys.argv[1]
goco = sys.argv[2]
goout = sys.argv[3]

def recom(string,start,end):
    start1 = int(start)-1
    end = int(end)
    b = string[start1:end]
    t = "-"
    for i in range(len(b)-1):
        t += "-"    
    string = string.replace(b,t)
    return string

fr=open( goin , 'r')
dict={}
for line in fr:
    if line.startswith('>'):
        name=line.strip()[1:]
        #print(name)
        dict[name]=''
    else:
        dict[name]+=line.replace('\n','')
print("finish")


control = open(goco ,"r")
lines = control.readlines()
for i in lines:
    line = i.split()
    a = line[0]
    b = line[1]
    c = line[2]
    dict[a] = recom(dict[a],b,c)
print("finish")
    
fw=open(goout, 'w')    
for i in dict.keys():
    print(">"+i,file = fw)
    print(dict[i].strip(),file = fw)

fr.close()
fw.close()
control.close()